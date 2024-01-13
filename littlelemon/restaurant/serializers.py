#define Serializer class for User model
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import MenuItem, booking

class MenuItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = booking
        fields = '__all__'


#class UserSerializer(serializers.ModelSerializer):

#    class Meta:
#        model = User   
#        fields = ['url', 'username', 'email', 'groups']

