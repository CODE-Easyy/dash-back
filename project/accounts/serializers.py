from rest_framework import serializers
from phonenumber_field.serializerfields import PhoneNumberField

from .models import Profile


class ProfileListSerializer(serializers.ModelSerializer):
    
    phone = PhoneNumberField()
    email = serializers.EmailField()
    
    class Meta:
        model = Profile
        fields = (
            'code',
            'full_name',
            'position',
            'phone',
            'email',
        )
