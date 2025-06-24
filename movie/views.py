from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from .models import Movie, Review
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required

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
  reviews = Review.objects.filter(movie = movie) #Using the filter function, we retrieve reviews for a particular movie only
  
  #  We then pass in the reviews to detail.html:
  return render(request, 'detail.html', {
    'movie': movie,
    'reviews': reviews
  })

def signUp(request): 
  email = request.GET.get('email')
  return render(request, 'signUp.html', {
    'email' : email
  })
  
@login_required
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
 
@login_required     
def updatereview(request, review_id): 
  # We first retrieve the review object with the review ID
  review = get_object_or_404(Review, pk=review_id, user=request.user)
  
  if request.method == 'GET': 
    form = ReviewForm(instance=review)
    return render(request, 'updatereview.html', {
      'review': review,
      'form': form
    })
  else: 
    try:
      form = ReviewForm(request.POST, instance=review)
      form.save()
      return redirect('movie_detail', review.movie.id) # type: ignore
    
    except ValueError: 
      return render(request, 'updatereview.html', {
        'review': review,
        'error': 'Bad data in form'
      })

@login_required
def deletereview(request, review_id):
  review = get_object_or_404(Review, pk=review_id, user=request.user)
  review.delete()
  return redirect('movie_detail', review.movie.id) # type: ignore
  