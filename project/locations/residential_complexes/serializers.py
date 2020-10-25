from rest_framework.serializers import ModelSerializer

from .models import ResidentalComplex

class ResidentalComplexSerializer(ModelSerializer):
    class Meta:
        model = ResidentalComplex
        fields = '__all__'
        