from rest_framework import serializers
from .models import Store
from goods.serializers import GoodsSerializer


class StoreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Store
        fields = ('id', 'name', 'last_visited', 'address', 'lat', 'lon')


# class GoodsInStoreSerializer(serializers.ModelSerializer):

#     goods = GoodsSerializer(many=True)

#     class Meta:
#         model = Store
#         fields = ('name', 'goods',)
