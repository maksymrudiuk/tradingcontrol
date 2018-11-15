from rest_framework import serializers
from ..models import UploadPhoto


class UploadPhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = UploadPhoto
        fields = ('file', 'created_at')
