from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login

def signupaccount(request):
  # If there´s a GET request it means that there's a user navigating to the sign up form via URL(localhost:8000/accounts/signupaccount) then we send them to the login form 
  if request.method == 'GET':
    return render(request, 'signupaccount.html', {
      'form': UserCreationForm
    })
  else: 
    if request.POST['password1'] == request.POST['password2'] : 
      user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
      user.save()
      login(request, user)
      return redirect('home')
    # If password1 doesn't match password2 
    else:
      return render(request, 'signupaccount.html', {
        'form': UserCreationForm, 
        'error': 'Passwords do not match'
        })
     
  
