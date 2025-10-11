from django.db import models

# Create your models here.
class TechPokemon(models.Model):
    name = models.CharField(max_length=100)
    skills = models.TextField()
    image_url = models.CharField(max_length=500, blank=True)
    difficulty = models.CharField(max_length=1, default='B')
    
    def __str__(self):
        return self.name
        
