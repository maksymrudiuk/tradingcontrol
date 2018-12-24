from rest_framework import serializers
from .models import RegisterKey


class RegisterKeyEmailSerialiazer(serializers.ModelSerializer):

    class Meta:
        model = RegisterKey
        fields = ('email',)
