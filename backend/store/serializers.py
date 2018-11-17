from rest_framework import serializers
from ..models import Store
from goods.serializers import GoodsSerializer


class StoreSerializer(serializers.ModelSerializer):

    goods = GoodsSerializer(many=True)

    class Meta:
        model = Store
        fields = ('id', 'name', 'address', 'goods')

    # def create(self, validated_data):
    #     assortments = validated_data.pop('store_assortment')
    #     store = Store.objects.create(**validated_data)
    #     for item in assortments:
    #         Goods.objects.create(shop=store, **item)
    #     return store
