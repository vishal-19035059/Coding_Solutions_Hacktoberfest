from operator import imod
from django.db import models
from location_field.models.plain import PlainLocationField
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.html import mark_safe
from django.conf import settings
from django.db.models.signals import pre_save
import os
from PIL import Image



# Create your models here.
class cycle_post(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    discription = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField()
    image = models.ImageField(upload_to='images/')
    city = models.CharField(max_length=200)
    location = PlainLocationField(based_fields=['city'], zoom=7)

    def __str__(self):
        return self.user.username+ '_' + self.title 