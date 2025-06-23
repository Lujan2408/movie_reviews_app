from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from .models import Movie, Review
from .forms import ReviewForm

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
  
def create_review(request, movie_id):
  # First get the object from db:
  movie = get_object_or_404(Movie, pk=movie_id)
  
  # pass in the review form for the user to create the review:
  if request.method == 'GET': 
    return render(request, 'createreview.html', {
      'form': ReviewForm(), 
      'movie': movie 
    })
  # When the user submits the createreview form, this function will receive a POST request, and we enter the else clause:
  else: 
    try: 
      # retrieve the submitted form from the req
      form = ReviewForm(request.POST)
      # create and save a new review object from the form's values but don't yet put it into the database (commit=False) because we want to specify the user and movie relationships for the review:
      newReview = form.save(commit=False) 
      # Finally, we specify the user and movie relationships for the review and save the review into the database:
      newReview.user = request.user
      newReview.movie = movie
      newReview.save()
      return redirect('movie_detail', newReview.movie_id)
    
    except ValueError: 
      return render(request, 'createreview.html', {
        'form': ReviewForm(), 
        'error': 'Bad data passed in'
      })