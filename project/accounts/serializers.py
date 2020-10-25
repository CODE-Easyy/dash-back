from rest_framework import serializers

from .models import Profile


class ProfileListSerializer(serializers.ModelSerializer):
    
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

class ProfileCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = (
            'full_name',
            'position',
            'phone',
            'email',
            'level'
        )
