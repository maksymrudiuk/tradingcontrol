from rest_framework import serializers
from .models import Region, City, Route
from user.serializers import UserProfileSerializer


class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = ('name',)


class RegionSerializer(serializers.ModelSerializer):

    city = CitySerializer()

    class Meta:
        model = Region
        fields = ('city', 'region')


class RouteSerializer(serializers.ModelSerializer):

    agent = UserProfileSerializer()
    route_region = RegionSerializer()

    class Meta:
        model = Route
        fields = ('agent', 'region', 'created')
