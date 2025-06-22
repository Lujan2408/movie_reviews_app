from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie

def home(request):
  searchTerm = request.GET.get('searchMovie')
  movies = Movie.objects.all()
  
  return render(request, 'home.html', {
    'searchTerm' : searchTerm,
    'movies': movies
  })

def about(request):
  return HttpResponse('<h1>Welcome to About Page</h1>')

def signUp(request): 
  email = request.GET.get('email')
  return render(request, 'signUp.html', {
    'email' : email
  })
  
  