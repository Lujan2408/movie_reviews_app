from django.db import models
from django.contrib.auth.models import User

class Movie (models.Model):
  title = models.CharField(max_length=100)
  description = models.CharField(max_length=250)
  image = models.ImageField(upload_to='movie/images')
  url = models.URLField(blank=True)
  
  def __str__(self): 
    return self.title

# ------------- Movie's review model ------------- #
# For all many-to-one relationships such as ForeignKey, we must also specify an on_delete option. This means that when you remove a user or movie, for instance, its associated reviews will be deleted as well. Note that this does not apply in the other direction – that is, when you remove a review, the associated movie and user still remain:
class Review(models.Model): 
  text = models.CharField(max_length=100)
  date = models.DateTimeField(auto_now_add=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE) # Allows to the user create multiple reviws, many-to-one relationship
  movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
  watchAgain = models.BooleanField()
  
  def __str__(self): 
    return self.text