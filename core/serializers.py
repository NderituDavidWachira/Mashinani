from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom fields to token payload
        token['is_superuser'] = user.is_superuser
        token['username'] = user.username
        token['user_type'] = user.user_type
        return token

# Serializer for creating new User instances with specific required fields
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'name', 'phone', 'user_type']
        extra_kwargs = {
            'username': {'required': True, 'error_messages': {'required': 'Username is required.'}},
            'password': {'write_only': True, 'required': True, 'error_messages': {'required': 'Password is required.'}},
            'name': {'required': False},
            'phone': {'required': False},
            'user_type': {'default': 'Employee'},
        }

    # Custom create method for handling password securely and providing tokens for direct login
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)  # Hash the password
        user.save()

        # Generate JWT tokens for direct login
        refresh = RefreshToken.for_user(user)
        return {
            'user': UserSerializer(user).data,
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
