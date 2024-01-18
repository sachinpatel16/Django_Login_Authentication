from django.http import HttpResponseRedirect
from django.shortcuts import render ,redirect
from .models import User
# Create your views here.


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = User.objects.create(username=username, email=email, password=password)
        
        return HttpResponseRedirect('/Login/')
    return render(request,'reg.html')

def login(request):
    if request.method == 'POST':
        email = request.POST.get('Email')
        password = request.POST.get('Password')
        
        try:
            user = User.objects.get(email=email, password=password)
            
            return HttpResponseRedirect('/home/')
        except User.DoesNotExist:
            pass
    return render(request,'login.html')

def home(request):
    return render(request,'home.html')