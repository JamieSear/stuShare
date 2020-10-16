from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

@receiver(post_save, sender=User) #when user is saved, send signal
def create_profile(sender, instance, created, **kwargs): #this signal is recieved 
    if created:
        Profile.objects.create(user=instance) #if created, create profile object with user equal to instance of the user that was created


@receiver(post_save, sender=User) 
def save_profile(sender, instance, created, **kwargs): 
    instance.profile.save()
        