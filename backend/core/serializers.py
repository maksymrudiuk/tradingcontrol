from rest_framework import serializers
from .models import UploadPhoto
from user.serializers import UserProfileSerializer
# from user.models import UserProfile


class UploadPhotoSerializer(serializers.ModelSerializer):

    owner = UserProfileSerializer(required=False)

    class Meta:
        model = UploadPhoto
        fields = ('file', 'created_at', 'owner')
