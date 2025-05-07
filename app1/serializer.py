from.models import*
from rest_framework import serializers
from django.contrib.auth.models import User

# class Studentserializer(serializers.ModelSerializer):
#     class Meta:
#         model=Student
#         fields='__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model=Movie
        fields='__all__'
class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model=Guest
        fields='__all__'
class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Reservation
        fields='__all__'
