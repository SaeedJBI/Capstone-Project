from django.contrib import admin
from .models import TechPokemon, UserProfile, TechTrack, UserPokemonCollection
# Register your models here.
admin.site.register(TechPokemon)
admin.site.register(UserProfile)
admin.site.register(TechTrack)
admin.site.register(UserPokemonCollection)