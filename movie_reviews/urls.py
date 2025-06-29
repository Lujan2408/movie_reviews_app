"""
URL configuration for movie_reviews project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from movie import views as movieViews
# Static media
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', movieViews.home, name='home'),
    path('signUp', movieViews.signUp, name='signUp'),
    path('news/', include('news.urls')), # path('news/', include('news.url')) will forward any requests with 'news/' to the news app's urls.py.
    path('movie/', include('movie.urls')),
    path('accounts/', include('accounts.urls'))
]

# With this, you can serve the static media from Django.
urlpatterns += static(settings.MEDIA_URL, 
    document_root=settings.MEDIA_ROOT)