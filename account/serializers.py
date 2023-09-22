from uuid import uuid4
import datetime
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers, validators

from .models import CustomUser, Profile 



class UserRegisterSerializer(serializers.ModelSerializer):
    
    email = serializers.EmailField(
        required=True, validators=[validators.UniqueValidator(queryset=CustomUser.objects.all())]
    )
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'password', 'password2')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        user = CustomUser.objects.create(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            custom_id = str(uuid4())[-12:]
        )
        user.set_password(validated_data['password'])
        user.save()
        Profile.objects.create(user=user)
        return user
    

class ProfileEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        exclude = ['user', 'id']


class UserEditSerializer(serializers.ModelSerializer):
    profile = ProfileEditSerializer(many=False)
    class Meta:
        model = CustomUser
        exclude = [
            'is_staff', 'is_active', 'date_joined', 'custom_id', 
            'is_worker', 'is_company', 'is_deleted', 'password',
            'is_superuser', 'groups', 'user_permissions'
        ]
    
    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile')
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if profile_data:
            # user = self.data['user']
            profile_db = Profile.objects.get(user=instance)
            print(profile_db)
            profile_serializer = ProfileEditSerializer(data=profile_data, partial=True)
            if profile_serializer.is_valid():
                profile_serializer.update(profile_db, profile_data)
        return instance


