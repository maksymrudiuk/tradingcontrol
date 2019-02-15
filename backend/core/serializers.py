from rest_framework import serializers
from .models import UploadPhoto
from user.serializers import UserProfileSerializer
from store.serializers import StoreSerializer


class UploadPhotoSerializer(serializers.ModelSerializer):

    owner = UserProfileSerializer(required=False)
    store = StoreSerializer(required=False)

    class Meta:
        model = UploadPhoto
        fields = ('file', 'created_at', 'store', 'owner')


class GetPhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = UploadPhoto
        fields = ('file',)
