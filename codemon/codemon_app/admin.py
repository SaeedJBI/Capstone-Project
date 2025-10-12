from django.contrib import admin
from .models import TechCodemon, UserProfile, TechTrack, UserCodemonCollection, QuizQuestion, TechSkill
# Register your models here.
admin.site.register(TechCodemon)
admin.site.register(UserProfile)
admin.site.register(TechTrack)
admin.site.register(UserCodemonCollection)
admin.site.register(QuizQuestion)
admin.site.register(TechSkill)