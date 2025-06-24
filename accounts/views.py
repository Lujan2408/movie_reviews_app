from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserCreateForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate # type: ignore
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required

def signupaccount(request):
  # If there´s a GET request it means that there's a user navigating to the sign up form via URL(localhost:8000/accounts/signupaccount) then we send them to the login form 
  if request.method == 'GET':
    return render(request, 'signupaccount.html', {
      'form': UserCreateForm
    })
    
  else: 
    if request.POST['password1'] == request.POST['password2'] : 
      
      try:
        user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
        user.save()
        login(request, user)
        return redirect('home')
      
      except IntegrityError:
        return render(request, 'signupaccount.html', {
          'form': UserCreateForm,
          'error': 'The Username entered already exists. Please choose a new Username to sign up'
        })    
        
    # If password1 doesn't match password2 
    else:
      return render(request, 'signupaccount.html', {
        'form': UserCreateForm, 
        'error': 'Passwords do not match'
        })
      
def loginaccount(request):
  if request.method == 'GET': 
    return render(request, 'loginaccount.html', {
      'form': AuthenticationForm
    })
  else: 
    user = authenticate(request, 
      username = request.POST['username'], 
      password = request.POST['password'])
    if user is None: 
      return render(request, 'loginaccount.html', {
        'form': AuthenticationForm(),
        'error': "Username and password don't match"
      })
    else: 
      login(request, user)
      return redirect('home')

@login_required
def logoutaccount(request): 
  logout(request)
  return redirect('home')