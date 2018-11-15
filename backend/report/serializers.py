from rest_framework import serializers
from ..models import ReportData, ReportItem


class ReportItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportItem
        fields = '__all__'


class ReportDataSerializer(serializers.ModelSerializer):

    assortment = ReportItemSerializer(many=True)

    class Meta:
        model = ReportData
        fields = ('id', 'name', 'assortment')

    def create(self, validated_data):
        assortments_data = validated_data.pop('assortment')
        report = report.objects.create(**validated_data)
        for assortment_data in assortments_data:
            ReportItem.objects.create(report=report, **assortment_data)
        return report
