from django.shortcuts import render
#from .models import 
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth.models import User

# Create your views here.

def home(request):
    users = User.objects.all()
    return render(request,'prof/index.html',{'users':users})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'prof/signup.html', {'form': form})