# Download modules
from django.utils import timezone
from django.http import JsonResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import (HTTP_400_BAD_REQUEST,
                                   HTTP_201_CREATED,
                                   HTTP_404_NOT_FOUND)
from rest_framework.authentication import SessionAuthentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

# Local modules
from store.models import Store
from location.models import Route
from .tasks import image_processing
from tradingcontrol.settings import DEBUG
from .serializers import UploadPhotoSerializer


# Create your views here.
class Upload(APIView):

    authentication_classes = (JSONWebTokenAuthentication,
                              SessionAuthentication)
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):

        if DEBUG:
            print(self.request.data)

        response = JsonResponse(
            {'error': 'user don`t have routes'},
            safe=False)

        if not Route.objects.filter(agent=self.request.user):
            return Response(response.content, status=HTTP_404_NOT_FOUND)

        else:

            errors = []
            upload_photos = []

            # parse data
            store_id = self.request.data['store_id']

            time_data = {}
            # time_data['t_start'] = self.request.data['t_start'][1:16]
            # time_data['t_finish'] = self.request.data['t_finish'][1:16]
            # time_data['t_delta'] = self.request.data['t_delta'][1:5]

            time_data['t_start'] = self.request.data['t_start']
            time_data['t_finish'] = self.request.data['t_finish']
            time_data['t_delta'] = self.request.data['t_delta']
            print(time_data)

            for file in self.request.data.getlist('files'):
                print(file)

                data = {'file': file, 'store_id': store_id}
                serializer = UploadPhotoSerializer(data=data)

                if serializer.is_valid():
                    serializer.save(owner=self.request.user)
                    upload_photos.append(serializer.data['file'])
                    # print(serializer.data)
                else:
                    errors.append(serializer.errors)

            if errors:
                return Response(errors, status=HTTP_400_BAD_REQUEST)
            else:
                print(timezone.now())
                store = Store.objects.get(id=store_id)
                store.last_visited = timezone.now().replace(microsecond=0)
                store.save()
                print('OK')
                image_processing.delay(upload_photos,
                                       store_id,
                                       time_data,
                                       str(self.request.user))
                return Response(upload_photos, status=HTTP_201_CREATED)
