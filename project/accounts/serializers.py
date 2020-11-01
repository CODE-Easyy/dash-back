from rest_framework import serializers

from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = (
            'code',
            'full_name',
            'position',
            'phone',
            'email',
            'level',
        )

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
    code = serializers.CharField(read_only=True)

    class Meta:
        model = Profile
        fields = (
            'code',
            'full_name',
            'position',
            'phone',
            'email',
            'level'
        )
