from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)
from django.db import models
from django.utils.translation import gettext_lazy as _
from rest_framework_simplejwt.tokens import RefreshToken


class UserManager(BaseUserManager):
    def create_user(self, password, email=None, **extra_fields):
        if not email:
            raise ValueError(_('The Phone must be set'))
        user = self.model(email=email, **extra_fields)
        user.email = self.normalize_email(email)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, password, email=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(password, email, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=50, verbose_name='Имя', null=True, blank=True)
    last_name = models.CharField(max_length=50, verbose_name='Фамилия', null=True, blank=True)
    email = models.EmailField(max_length=255, null=True, blank=True, unique=True)
    avatar = models.ImageField(upload_to='profile/images/', verbose_name='Аватар', null=True, blank=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    confirmation_code = models.CharField(verbose_name='Код подтверждения', max_length=6, null=True, blank=True, )
    USERNAME_FIELD = 'email'
    objects = UserManager()

    def __str__(self):
        return f'{self.last_name} {self.first_name}'

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {'refresh': str(refresh), 'access': str(refresh.access_token)}
