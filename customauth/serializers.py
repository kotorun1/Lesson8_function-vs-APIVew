from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import CustomUser


# Сериализатор для модели пользователя
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username','email', 'password')
        extra_kwargs = {'password': {'write_only': True, 'min_length': 8}}

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)

# Сериализатор для авторизации пользователя
class AuthTokenSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(style={'input_type': 'password'})

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        user = authenticate(request=self.context.get('request'),
                            email=email, password=password)
        if not user:
            raise serializers.ValidationError('Неверные данные для входа. Пожалуйста, попробуйте еще раз.')

        attrs['user'] = user # добавляем поле user в словарь attrs

        return attrs

