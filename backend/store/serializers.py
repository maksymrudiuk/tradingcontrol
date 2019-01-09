from rest_framework import serializers
from .models import Store, GoodsInStore
from goods.serializers import GoodsSerializer
from location.serializers import RegionSerializer


class StoreSerializer(serializers.ModelSerializer):

    # goods = GoodsSerializer(many=True)
    # store_region = RegionSerializer()

    class Meta:
        model = Store
        fields = ('id', 'name', 'last_visited', 'address', 'lat', 'lon')


class GoodsInStoreSerializer(serializers.ModelSerializer):

    goods = GoodsSerializer(many=True)

    class Meta:
        model = Store
        fields = ('name', 'goods',)
