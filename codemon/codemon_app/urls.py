from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('codemon/', views.codemon_list, name='codemon-list'),
    path('accounts/signup/', views.signup, name='signup'),
]