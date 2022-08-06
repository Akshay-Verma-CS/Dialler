from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["UserName","phoneNumber","email"]

class RegisterSerializer(serializers.ModelSerializer):
    name  = serializers.CharField(
        required = True,
        validators = [UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(
        write_only = True,
        required = True , validators = [validate_password])
    password2 = serializers.CharField(write_only=True,required=True)
    class Meta:
        model = User
        fields = ('userName','password','password2','email')
        extra_Kwargs = {
            'name':{'required':True},
            }
    def validate(self,attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password":"Password fields didn't match."})
        return attrs
    def create(self,validated_data):
        user = user.objects.create(
            username = validated_data['userName'],
            email = validated_data['email'],
            name = validated_data['name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user