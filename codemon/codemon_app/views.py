from django.shortcuts import render
from .models import TechPokemon
# Create your views here.
def home(request):
    return render(request, 'home.html')

def pokemon_list(request):
    pokemons = TechPokemon.objects.all()
    return render(request, 'pokemon/list.html', {'pokemons': pokemons})