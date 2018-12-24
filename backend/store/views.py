from rest_framework.response import Response
from django.http import JsonResponse
from .serializers import StoreSerializer, GoodsInStoreSerializer
from .models import Store
from django.shortcuts import get_object_or_404
from location.models import Route
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication
from rest_framework import viewsets

# Create your views here.

class StoreViewSet(viewsets.ViewSet):

    authentication_classes = (JSONWebTokenAuthentication,
                              SessionAuthentication)
    permission_classes = (IsAuthenticated,)

    # def list(self, request, format=None):

    #     try:
    #         route = Route.objects.get(agent=self.request.user)
    #         store = Store.objects.filter(store_region=route.route_region)
    #         serializer = StoreSerializer(store, many=True)
    #         return Response(serializer.data)
    #     except Exception:
    #         response = JsonResponse(
    #             {'error': 'routes doesn`t exist'},
    #             safe=False)
    #         return Response(response.content)

    def list(self, request, format=None):
        store = Store.objects.all()
        serializer = StoreSerializer(store, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Store.objects.all()
        store = get_object_or_404(queryset, pk=pk)
        serializer = GoodsInStoreSerializer(store)
        return Response(serializer.data)


class GoodsInStoreList(APIView):

    authentication_classes = (JSONWebTokenAuthentication,
                              SessionAuthentication)
    permission_classes = (IsAuthenticated,)

    def get(self, request, store, format=None):
        # store_id = self.request.query_params.get('id')
        store = Store.objects.filter(id=self.store)
        serializer = GoodsInStoreSerializer(store, many=True)
        return Response(serializer.data)
