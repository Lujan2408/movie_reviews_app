from django.shortcuts import render
from .models import New

def news(request): 
  news = New.objects.all().order_by('-date') # Display the most recent new
  return render(request, "news.html", {
    'news': news
  })