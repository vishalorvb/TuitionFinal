from django.db import models
from django.contrib.auth.models import AbstractUser
from django.forms import CharField
from .manager import *



class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=12 , unique=True)
    Full_name = models.CharField(max_length=55)
    email = models.EmailField(max_length=60,null=True  , blank=True)
    credit_points = models.IntegerField(default=0)
    profilepic = models.ImageField(upload_to='images',default="profilepic.png")
    username = None
    first_name = None
    last_name= None
    
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.Full_name

    object = CustomUserManager()
   




