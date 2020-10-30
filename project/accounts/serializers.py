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
            'is_admin'
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
