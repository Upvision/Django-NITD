from allauth.account.adapter import get_adapter
from rest_auth.registration.serializers import RegisterSerializer
from django.urls import path, include
from core import models
from rest_framework import routers, serializers, viewsets

from rest_framework.authtoken.models import Token



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'profile_pic']


class CustomRegisterSerializer(RegisterSerializer):
    first_name = serializers.CharField(allow_blank=True, allow_null=True)
    last_name = serializers.CharField(allow_blank=True, allow_null=True)
    email = serializers.EmailField(allow_blank = True, allow_null=True)
    profile_pic = serializers.ImageField(max_length=None, allow_empty_file=True, use_url=True)

    class Meta:
        model = models.User
        fields = ('email', 'username', 'password', 'first_name', 'last_name', 'profile_pic')

    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'first_name': self.validated_data.get('first_name', ''),
            'last_name': self.validated_data.get('last_name', ''),
            'password1': self.validated_data.get('password1', ''),
            'password2': self.validated_data.get('password2', ''),
            'email': self.validated_data.get('email', ''),
            'profile_pic': self.validated_data.get('profile_pic', ''),
        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        user.save()
        adapter.save_user(request, user, self)
        return user

class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = ('key', 'user')


class DegreeLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DegreeLevel
        fields = "__all__"

class DepartmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Department
        fields = "__all__"




