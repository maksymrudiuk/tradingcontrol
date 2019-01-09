from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import Store
from .serializers import StoreSerializer, GoodsInStoreSerializer

# Create your views here.


class StoreViewSet(viewsets.ViewSet):

    authentication_classes = (JSONWebTokenAuthentication,
                              SessionAuthentication)
    permission_classes = (IsAuthenticated,)

    def list(self, request, format=None):
        store = Store.objects.all()
        serializer = StoreSerializer(store, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Store.objects.all()
        store = get_object_or_404(queryset, pk=pk)
        serializer = GoodsInStoreSerializer(store)
        return Response(serializer.data)
