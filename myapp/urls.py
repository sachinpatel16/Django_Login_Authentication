# myapp/urls.py
from django.urls import path
from myapp import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('Login/', views.login, name='login'),
    path('home/', views.home, name='dashboard'),
]
