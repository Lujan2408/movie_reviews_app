from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
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
  
def movie_detail(request, movie_id): 
  # We use get_object_or_404 to get the specific movie object we want.
  # We provide movie_id as the primary key, pk=movie_id. If there is a match, get_object_or_404, as its name suggests, returns us the object or the not found (404) object.
  movie = get_object_or_404(Movie, pk=movie_id)
  return render(request, 'detail.html', {
    'movie': movie
  })

def about(request):
  return HttpResponse('<h1>Welcome to About Page</h1>')

def signUp(request): 
  email = request.GET.get('email')
  return render(request, 'signUp.html', {
    'email' : email
  })
  
  