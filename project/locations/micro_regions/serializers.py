from rest_framework.serializers import ModelSerializer

from .models import MicroRegion

class MicroRegionSerializer(ModelSerializer):
    class Meta:
        model = MicroRegion
        fields = '__all__'
        