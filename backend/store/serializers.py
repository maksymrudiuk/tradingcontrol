from rest_framework import serializers
from .models import Store


class StoreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Store
        fields = ('id', 'name', 'last_visited',
                  'address', 'lat', 'lon', 'work_radius')
