from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('codemon/', views.codemon_list, name='codemon-list'),
    path('accounts/signup/', views.signup, name='signup'),
    path('battle/encounter/', views.encounter_codemon, name='battle-encounter'),
    path('battle/start/<int:codemon_id>/', views.battle_start, name='battle-start'),
    path('battle/submit/<int:codemon_id>/', views.battle_submit, name='battle-submit'),
    path('collection/', views.my_collection, name='my-collection'),
    path('claim-daily-bonus/', views.claim_daily_bonus, name='claim-daily-bonus'),
    path('codemon/create/', views.CodemonCreate.as_view(), name='codemon-create'),
    path('codemon/<int:pk>/update/', views.CodemonUpdate.as_view(), name='codemon-update'),
    path('codemon/<int:pk>/delete/', views.CodemonDelete.as_view(), name='codemon-delete'),
]