from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed, ValidationError

from users.models import User


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password')

    def to_representation(self, instance):
        data = super(RegisterSerializer, self).to_representation(instance)
        data.pop('password')
        return data


class VerifyEmailSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=4)
    email = serializers.EmailField()

    class Meta:
        fields = ('code', 'email')

    def validate(self, attrs):
        email = attrs.get('email')
        code = attrs.get('code')
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise ValidationError('Пользователь не существует.')
        if user.confirmation_code != code:
            raise ValidationError('Код указан неверно')
        user.is_active = True
        user.is_verified = True
        user.save()
        return attrs

    def to_representation(self, instance):
        user = User.objects.get(email=instance.get('email'))
        return {'token': user.tokens()}


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(min_length=6, max_length=40)

    class Meta:
        fields = ('email', 'password')
