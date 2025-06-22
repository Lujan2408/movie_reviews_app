from django.db import models

class New(models.Model): 
  headline = models.CharField(max_length=200)
  body = models.TextField()
  date = models.DateField()

  #  The __str__ method represents the class objects as a string: __str__ will be called when the news objects are listed in admin
  def __str__(self):
    return self.headline

# To make migrations: 
# python manage.py makemigrations
# python manage.py migrate