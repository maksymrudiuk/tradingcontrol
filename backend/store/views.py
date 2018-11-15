from rest_framework.response import Response
from .serializers import StoreSerializer
from .models import Store
from rest_framework.views import APIView
from rest_framework.permissions import (AllowAny,
                                        IsAuthenticated)

# Create your views here.


class StoreList(APIView):

    # permission_classes = (IsAuthenticated,)
    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        shop = Store.objects.all()
        serializer = StoreSerializer(shop, many=True)
        return Response(serializer.data)
