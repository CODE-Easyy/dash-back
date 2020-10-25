from rest_framework.serializers import ModelSerializer

from .models import AdministrativeRegion

class AdministrativeRegionSerializer(ModelSerializer):
    class Meta:
        model = AdministrativeRegion
        fields = '__all__'
        