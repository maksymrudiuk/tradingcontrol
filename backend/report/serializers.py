from rest_framework import serializers
from .models import ReportData, ReportItem
from user.serializers import UserProfileSerializer
from store.serializers import StoreSerializer


class ReportItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportItem
        fields = ('name', 'status')


class ReportDataSerializer(serializers.ModelSerializer):

    owner = UserProfileSerializer(required=False)
    store = StoreSerializer(required=False)
    assortment = ReportItemSerializer(many=True)

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
