from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class TechPokemon(models.Model):
    name = models.CharField(max_length=100)
    skills = models.TextField()
    image_url = models.CharField(max_length=500, blank=True)
    difficulty = models.CharField(max_length=1, default='B')
    
    def __str__(self):
        return self.name
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    available_rolls = models.IntegerField(default=3)
    last_daily_roll = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.user.username}'s profile"

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    

        
