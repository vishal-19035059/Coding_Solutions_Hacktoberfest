

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




class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_img = models.ImageField(default='profile_img/default.jpg', upload_to='profile_img/', blank=True)
    bio = models.TextField(max_length=500, blank=True, default="Hii, write your bio here")
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.profile_img.path) # Open image
        # resize image
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size) # Resize image
            img.save(self.profile_img.path) # Save it again and override the larger image
    
    def thumbnail(self):
        return mark_safe(f'<img src="{self.profile_img.url}" width="50" height="50" />'.format(self.profile_img.url))


# delete profie pic on setting a new one 
@receiver(pre_save, sender=Profile)
def delete_old_file(sender, instance, **kwargs):
    # on creation, signal callback won't be triggered 
    if instance._state.adding and not instance.pk:
        return False
    try:
        old_file = sender.objects.get(pk=instance.pk).profile_img
    except sender.DoesNotExist:
        return False
    
    # comparing the new file with the old one
    file = instance.profile_img
    if not old_file == file:
        if os.path.isfile(old_file.path):
            if old_file.url != 'profile_img/default.jpg':
                os.remove(old_file.path)
    
    
# create profile model on creating user 
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

# save profile on creating user model 
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()





# 15 march 
# 3 march 