from rest_framework import serializers
from .models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):

    role = serializers.CharField(source='get_role_display')

    class Meta:
        model = UserProfile
        fields = ('username', 'first_name', 'last_name', 'email', 'role')
