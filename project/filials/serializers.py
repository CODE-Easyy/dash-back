from rest_framework import serializers

from .models import Filial

class FilialListSerializer(serializers.ModelSerializer):
    city_name = serializers.RelatedField(
        source='city', 
        read_only=True
    )

    class Meta:
        model = Filial
        fields = (
            'id',
            'name',
            'city_name',
            'actual_address',
        )
