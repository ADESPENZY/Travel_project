from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegistrationForm
from django.contrib.auth import authenticate , login, logout
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def login_page(request):
    if request.user.is_authenticated:
        return redirect('home_page')
    
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email , password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            return redirect('home_page')
        else:
            messages.error(request, 'Something went wrong. Please check your credentials.')
            return redirect('login_page')
    
    return render(request, 'home.html')


def register_page(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            var = form.save(commit = False)
            var.username = var.email
            var.save()
            messages.info(request, 'your account have been created successfully')
            return redirect('login_page')
        else:
            messages.error(request, 'something went wrong')
            return redirect('register_page') 
    else:
        form = RegistrationForm(request.POST)
    
        return render(request, 'account/register.html')


def logout_page(request):
    if request.method == 'POST':
       logout(request)
       return redirect('home_page')

    

    