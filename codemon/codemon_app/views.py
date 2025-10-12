from django.shortcuts import render, redirect
from .models import TechCodemon
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
import random

# Create your views here.
def home(request):
    return render(request, 'home.html')

def codemon_list(request):
    codemons = TechCodemon.objects.all()
    return render(request, 'codemon/list.html', {'codemons': codemons})


def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('codemon-list')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

@login_required
def encounter_codemon(request):
    user_profile = request.user.userprofile
    
    if user_profile.available_rolls < 1:
        return render(request, 'battle/no_rolls.html')
    
    user_profile.available_rolls -= 1
    user_profile.save()
    
    available_codemon = TechCodemon.objects.all()
    encountered_codemon = random.choice(available_codemon)
    
    return render(request, 'battle/encounter.html', {
        'codemon': encountered_codemon,
        'rolls_remaining': user_profile.available_rolls
    })

@login_required
def battle_start(request, codemon_id):
    # will build it later ...
    return render(request, 'battle/placeholder.html', {
        'message': f'Battle system coming soon! Codemon ID: {codemon_id}'
    })