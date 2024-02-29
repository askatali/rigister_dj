from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView, UpdateAPIView
from rest_framework import status
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate

from .service import send_email, generate_code
from .serializers import (
    RegisterSerializer,
    VerifyEmailSerializer,
    LoginSerializer,
    ProfileUpdateSerializer
)
from .models import User


class RegisterView(GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        code = generate_code()
        user = serializer.save(
            confirmation_code=code,
            password=make_password(serializer.validated_data.get("password"))
        )
        send_email(code, user.email)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class VerifyEmailView(GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = VerifyEmailSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class LoginView(GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data.get("email")
        password = serializer.validated_data.get("password")
        user = authenticate(email=email, password=password)
        if user:
            if user.is_verified:
                return Response({"token": user.tokens()}, status=status.HTTP_200_OK)
            return Response({"message": "Аккаунт не подтвержден"}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'Электронный почта или пароль не верный'}, status=status.HTTP_200_OK)


class UserProfileDetailView(GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProfileUpdateSerializer

    def get_object(self):
        return self.request.user

    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(self.get_object(), many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProfileUpdateView(UpdateAPIView):
    permission_classes = [AllowAny]
    serializer_class = ProfileUpdateSerializer


    def get_queryset(self):
        return self.request.user

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_queryset()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)

