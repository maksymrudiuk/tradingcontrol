# from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.status import HTTP_404_NOT_FOUND
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from location.models import Route
from user.models import UserProfile
from .models import Store, GoodsInStore
from .serializers import StoreSerializer
from goods.serializers import GoodsSerializer


# Create your views here.


class StoreViewSet(viewsets.ViewSet):

    authentication_classes = (JSONWebTokenAuthentication,
                              SessionAuthentication)
    permission_classes = (IsAuthenticated,)

    def list(self, request, format=None):

        if self.request.user.isDirector:
            staff = UserProfile.objects.filter(
                company=self.request.user.company)
            routes = Route.objects.filter(
                agent__in=staff)

            regions = []
            for route in routes:
                regions.append(route.route_region)

            queryset = (Store.objects.filter(
                store_region__in=regions))

            print(queryset)

        if self.request.user.isAgent:

            try:
                user_route = Route.objects.get(agent=self.request.user)
            except ObjectDoesNotExist:
                return Response(status=HTTP_404_NOT_FOUND)

            queryset = Store.objects.filter(
                store_region=user_route.route_region)

        if self.request.user.username == 'admin':
            print('Superuser')
            queryset = Store.objects.all()

        serializer = StoreSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = GoodsInStore.objects.filter(store_id=pk)
        goods = []
        for itm in queryset:
            goods.append(itm.goods)
        serializer = GoodsSerializer(goods, many=True)
        return Response(serializer.data)

    # def retrieve(self, request, pk=None):
    #     queryset = Store.objects.all()
    #     store = get_object_or_404(queryset, pk=pk)
    #     serializer = GoodsInStoreSerializer(store)
    #     return Response(serializer.data)
