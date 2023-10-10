from rest_framework import serializers

from .models import CustomUser


class UserSignUpSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)
    class Meta:
        model=CustomUser
        fields=("email","first_name","last_name", "password")