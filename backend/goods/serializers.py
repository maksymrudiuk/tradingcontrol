from rest_framework import serializers
from .models import Goods


class GoodsSerializer(serializers.ModelSerializer):

    category = serializers.CharField(source='get_category_display')

    class Meta:
        model = Goods
        fields = ('name', 'category')


class GoodsWithImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Goods
        fields = ('name', 'image')
