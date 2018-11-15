from rest_framework.response import Response
from .serializers import UploadPhotoSerializer
from rest_framework.views import APIView
from rest_framework.permissions import (AllowAny,
                                        IsAuthenticated)
from rest_framework.status import (HTTP_400_BAD_REQUEST,
                                   HTTP_201_CREATED)
# from .tasks import detect, test
from .tasks import detect


# Create your views here.
class Upload(APIView):

    # permission_classes = (IsAuthenticated,)
    permission_classes = (AllowAny,)

    def post(self, request, format=None):

        errors = []
        upload_photos = []

        for file in self.request.data.getlist('files[]'):
            data = {'file': file}
            serializer = UploadPhotoSerializer(data=data)

            if serializer.is_valid():
                serializer.save()
                upload_photos.append(serializer.data['file'])
            else:
                errors.append(serializer.errors)

        if errors:
            return Response(errors, status=HTTP_400_BAD_REQUEST)
        else:
            return Response(upload_photos, status=HTTP_201_CREATED)
