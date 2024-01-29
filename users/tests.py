from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken
from django.test import TestCase

from users.models import User
from users.serializers import (
    RegisterSerializer,
    LoginSerializer,
    UserProfileSerializer,
    VerifyEmailSerializer
)


class UserApiTests(APITestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(
            email='admin@test.com',
            password='password',
            is_active=True,
            is_verified=True,
            confirmation_code=4567
        )

    @property
    def bearer_token(self):
        refresh = RefreshToken.for_user(self.user1)
        return {"HTTP_AUTHORIZATION": f'Bearer {refresh.access_token}'}

    def test_register(self):
        data = {
            'email': 'admin2@test.com',
            'password': 'password2'
        }
        response = self.client.post(reverse('register'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_verify_email(self):
        data = {
            'email': 'admin@test.com',
            'code': 4567
        }
        response = self.client.post(reverse('verify_email'), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_login(self):
        data = {
            'email': 'admin@test.com',
            'password': 'password'
        }
        response = self.client.post(reverse('login'), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_profile(self):
    #     response = self.client.get(reverse('profile'), **self.bearer_token)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_update_profile(self):
    #     data = {
    #         'first_name': 'Arsen',
    #         'last_name': 'Kenjegulov'
    #     }
    #     response = self.client.put(reverse('update_profile'), data, **self.bearer_token)
        # self.assertEqual(response.status_code, status.HTTP_200_OK)


class TestUserSerializer(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(
            email='admin@test.com',
            password='password',
            is_active=True,
            is_verified=True,
            confirmation_code=4567
        )

    def test_register(self):
        data = {
            'first_name': 'John',
            'last_name': 'Kuper',
            'email': 'admin2@test.com',
            'password': 'password'
        }
        serializer = RegisterSerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_login(self):
        data = {
            'email': 'admin@test.com',
            'password': 'password'
        }
        serializer = LoginSerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_verify_email(self):
        data = {
            'email': 'admin@test.com',
            'code': 4567
        }
        serializer = VerifyEmailSerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_profile(self):
        data = {
            'first_name': 'John',
            'last_name': 'Kuper'
        }
        serializer = UserProfileSerializer(data=data)
        self.assertTrue(serializer.is_valid())
