from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('codemon/', views.codemon_list, name='codemon-list'),
    path('accounts/signup/', views.signup, name='signup'),
    path('battle/encounter/', views.encounter_codemon, name='battle-encounter'),
    path('battle/start/<int:codemon_id>/', views.battle_start, name='battle-start'),
    path('battle/submit/<int:codemon_id>/', views.battle_submit, name='battle-submit'),
]