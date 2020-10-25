from rest_framework import serializers

from .models import Filial

class FilialListSerializer(serializers.ModelSerializer):
    city = serializers.CharField(source='city.name')

    class Meta:
        model = Filial
        fields = (
            'id',
            'name',
            'city',
            'actual_address',
        )
