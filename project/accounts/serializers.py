from rest_framework import serializers

from .models import Profile

class RequestsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = (
            'code',
            'full_name',
            'email',
            'phone'
        )

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


class ProfileDetailSerializer(serializers.ModelSerializer):
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


class ProfileCreateSerializer(serializers.ModelSerializer):
    code = serializers.CharField(read_only=True)

    def create(self, validated_data):
        profile = Profile(**validated_data)
        profile.set_password(validated_data.get('password'))
        profile.is_active = True
        if profile.level == 'Супер Администратор':
            profile.is_staff = True
            profile.is_superuser = True
        profile.save()
        return profile

    def update(self, instance, validated_data):
        instance.full_name = validated_data.get(
            'full_name', instance.full_name)
        instance.position = validated_data.get('position', instance.position)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.email = validated_data.get('email', instance.email)
        instance.level = validated_data.get('level', instance.level)
        try:
            if not instance.check_password(validated_data.get('password')):
                instance.set_password(validated_data.get('password'))
        except:
            ...
        instance.save()
        return instance

    class Meta:
        model = Profile
        fields = (
            'code',
            'full_name',
            'position',
            'phone',
            'email',
            'level',
            'password'
        )
