from django.db import models

class New(models.Model): 
  headline = models.CharField(max_length=200)
  body = models.TextField()
  date = models.DateField()

# To make migrations: 
# python manage.py makemigrations
# python manage.py migrate