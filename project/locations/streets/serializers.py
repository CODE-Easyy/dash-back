from rest_framework.serializers import ModelSerializer

from .models import Street

class StreetSerializer(ModelSerializer):
    class Meta:
        model = Street
        fields = '__all__'
        