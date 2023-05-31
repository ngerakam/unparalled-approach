from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from rest_framework import serializers
from .models import *


class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = [
            "id",
            "first_name",
            "last_name",
            "username",
            "email",
            "password",
        ]


class UserProfileSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.user.id")

    class Meta:
        model = UserProfile
        fields = "__all__"
