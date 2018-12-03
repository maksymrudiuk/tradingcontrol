# Download modules
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import (IsAuthenticated)
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.status import (HTTP_400_BAD_REQUEST,
                                   HTTP_201_CREATED)

# Local modules
from .tasks import image_processing
from .serializers import UploadPhotoSerializer


# Create your views here.
class Upload(APIView):

    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):

        errors = []
        upload_photos = []

        store_id = 1  # must be dynamic value

        for file in self.request.data.getlist('files[]'):

            data = {'file': file}
            serializer = UploadPhotoSerializer(data=data)

            if serializer.is_valid():
                serializer.save(owner=self.request.user)
                upload_photos.append(serializer.data['file'])
            else:
                errors.append(serializer.errors)

        if errors:
            return Response(errors, status=HTTP_400_BAD_REQUEST)
        else:
            image_processing.delay(upload_photos,
                                   store_id,
                                   str(self.request.user))
            return Response(upload_photos, status=HTTP_201_CREATED)
