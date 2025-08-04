from rest_framework import serializers  
from a_users.models import User
from django.contrib.auth import authenticate

class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True)
    
    class Meta:
        model = User
        fields = ['email' , 'username' , 'password']
        
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    
    def validate(self, data): ##
        user = authenticate(email = data['email'] , password = data['password'])
        if not user :
            raise serializers.ValidationError('Invlaid Credentials')
        data['user'] = user
        return data
    