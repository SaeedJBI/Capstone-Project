from django.shortcuts import render, redirect
from .models import TechCodemon, QuizQuestion
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
    
    codemon = TechCodemon.objects.get(id=codemon_id)
    
    codemon_skills = codemon.skills.all()
    questions = QuizQuestion.objects.filter(
        skills__in=codemon_skills,
        difficulty=codemon.difficulty
    ).distinct()[:5]
    
    if questions.count() < 5:
        additional_questions = QuizQuestion.objects.filter(
            skills__in=codemon_skills
        ).exclude(id__in=[q.id for q in questions]).distinct()[:5-questions.count()]
        questions = list(questions) + list(additional_questions)
    
    battle_questions = []
    for question in questions:
        answers = [
            question.correct_answer,
            question.wrong_answer1,
            question.wrong_answer2,
            question.wrong_answer3
        ]
        random.shuffle(answers)
        battle_questions.append({
            'question': question,
            'answers': answers,
            'correct_answer': question.correct_answer
        })

    return render(request, 'battle/battle.html', {'codemon': codemon, 'questions': battle_questions})

@login_required
def battle_submit(request, codemon_id):
    # Temporary placeholder 
    return render(request, 'battle/placeholder.html', {
        'message': f'Battle submission coming soon! Codemon ID: {codemon_id}'
    })