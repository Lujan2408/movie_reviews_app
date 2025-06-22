from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie

def home(request):
  searchTerm = request.GET.get('searchMovie')
  if searchTerm: 
#   If a search term is entered, we call the model's filter method to return the movie 
#   objects with a case-insensitive match to the search term:
    movies = Movie.objects.filter(title__icontains=searchTerm)
  else: 
    movies = Movie.objects.all()
  return render(request, 'home.html', {
    'searchTerm' : searchTerm,
    'movies' : movies
  })
  

def about(request):
  return HttpResponse('<h1>Welcome to About Page</h1>')

def signUp(request): 
  email = request.GET.get('email')
  return render(request, 'signUp.html', {
    'email' : email
  })
  
  