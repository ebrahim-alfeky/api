from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.

# class Student(models.Model):
#     fname=models.CharField( max_length=25)
#     lname=models.CharField( max_length=25)
#     department=models.CharField( max_length=25)
#     age=models.IntegerField()
#     degree=models.FloatField()
#     date=models.DateTimeField(auto_now_add=True)
#     def __str__(self):
#         return self.fname+" "+self.lname+'  '+str(self.id)

class Movie(models.Model):
    hall = models.CharField(max_length=10)
    movie = models.CharField(max_length=50)
    date = models.DateField(auto_now=True)
    created_by=models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)
    def __str__(self):
        return self.movie
    
    
class Guest(models.Model):
    name = models.CharField(max_length=50)
    mobile = models.CharField(max_length=15)
    def __str__(self):
        return self.name

class Reservation(models.Model):
    guests=models.ForeignKey("app1.Guest", related_name='guests_names',on_delete=models.CASCADE,null=True)
    movies=models.ForeignKey('app1.Movie', related_name='movies_names',on_delete=models.CASCADE,null=True )



    