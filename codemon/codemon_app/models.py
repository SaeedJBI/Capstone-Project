from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class TechSkill(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
    
class TechTrack(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    color = models.CharField(max_length=20, default='#3498db')
    
    def __str__(self):
        return self.name


class TechCodemon(models.Model):
    DIFFICULTY_CHOICES = [
        ('B', 'Beginner'),
        ('I', 'Intermediate'),
        ('A', 'Advanced'),
    ]

    name = models.CharField(max_length=100)
    skills = models.ManyToManyField(TechSkill)
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
    
    def can_claim_daily_bonus(self):
        from django.utils import timezone
        today = timezone.now().date()
        return self.last_daily_roll != today
    
    

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    
class UserCodemonCollection(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    codemon = models.ForeignKey(TechCodemon, on_delete=models.CASCADE)
    captured_date = models.DateTimeField(auto_now_add=True)
    capture_score = models.IntegerField(null=True, blank=True)  
    
    class Meta:
        unique_together = ['user', 'codemon']
    
    def __str__(self):
        return f"{self.user.username} - {self.codemon.name}"
        
#_________________________

class QuizQuestion(models.Model):
    DIFFICULTY_CHOICES = [
        ('B', 'Beginner'),
        ('I', 'Intermediate'),
        ('A', 'Advanced'),
    ]
    
    question_text = models.TextField()
    correct_answer = models.CharField(max_length=200)
    wrong_answer1 = models.CharField(max_length=200)
    wrong_answer2 = models.CharField(max_length=200)
    wrong_answer3 = models.CharField(max_length=200)
    skills = models.ManyToManyField(TechSkill)
    difficulty = models.CharField(max_length=1, choices=DIFFICULTY_CHOICES, default='B')
    
    def __str__(self):
        return f"{self.question_text[:50]}..."