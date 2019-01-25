from rest_framework import serializers
from .models import ReportData, ReportItem
from user.serializers import UserProfileSerializer
from store.serializers import StoreSerializer
from goods.serializers import GoodsWithImageSerializer


class ReportItemPOSTSerializer(serializers.ModelSerializer):

    # goods_item = GoodsWithImageSerializer()

    class Meta:
        model = ReportItem
        fields = ('goods_item', 'status')


class ReportItemGETSerializer(serializers.ModelSerializer):

    goods_item = GoodsWithImageSerializer()

    class Meta:
        model = ReportItem
        fields = ('goods_item', 'status')


class ReportDataGETSerializer(serializers.ModelSerializer):

    owner = UserProfileSerializer(required=False)
    store = StoreSerializer(required=False)
    assortment = ReportItemGETSerializer(many=True)

    class Meta:
        model = ReportData
        fields = ('id', 'name', 'owner', 'store',
                  't_start', 't_finish', 't_delta',
                  'assortment_percent', 'assortment', 'created_at')

    def create(self, validated_data):
        assortments_data = validated_data.pop('assortment')
        report = ReportData.objects.create(**validated_data)
        for assortment_data in assortments_data:
            ReportItem.objects.create(report=report, **assortment_data)
        return report


class ReportDataPOSTSerializer(serializers.ModelSerializer):

    owner = UserProfileSerializer(required=False)
    store = StoreSerializer(required=False)
    assortment = ReportItemPOSTSerializer(many=True)

    class Meta:
        model = ReportData
        fields = ('id', 'name', 'owner', 'store',
                  't_start', 't_finish', 't_delta',
                  'assortment_percent', 'assortment', 'created_at')

    def create(self, validated_data):
        assortments_data = validated_data.pop('assortment')
        report = ReportData.objects.create(**validated_data)
        for assortment_data in assortments_data:
            ReportItem.objects.create(report=report, **assortment_data)
        return report
