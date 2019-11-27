from rest_framework import serializers
from .models import UserProfile,ProfileFeed

class HelloSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=10)
    last_name = serializers.CharField(max_length=10)
    

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id','email','first_name','last_name','password']
        extra_kwargs = {'password':{'write_only':True}}

    def create(self,validated_data):
        # create and return a new user
        user = UserProfile(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class ProfileFeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileFeed
        fields = ['id','user_profile','status_text','created_date']
        extra_kwargs = {'user_profile':{'read_only':True}}