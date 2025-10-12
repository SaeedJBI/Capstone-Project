from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class TechTrack(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    color = models.CharField(max_length=20, default='#3498db')
    
    def __str__(self):
        return self.name


class TechPokemon(models.Model):
    DIFFICULTY_CHOICES = [
        ('B', 'Beginner'),
        ('I', 'Intermediate'),
        ('A', 'Advanced'),
    ]

    name = models.CharField(max_length=100)
    skills = models.TextField()
    image_url = models.CharField(max_length=500, blank=True)
    difficulty = models.CharField(max_length=1, choices=DIFFICULTY_CHOICES, default='B')
    tech_track = models.ForeignKey(TechTrack, on_delete=models.CASCADE)
    
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
    
class UserPokemonCollection(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    pokemon = models.ForeignKey(TechPokemon, on_delete=models.CASCADE)
    captured_date = models.DateTimeField(auto_now_add=True)
    capture_score = models.IntegerField(null=True, blank=True)  
    
    class Meta:
        unique_together = ['user', 'pokemon']
    
    def __str__(self):
        return f"{self.user.username} - {self.pokemon.name}"
        
