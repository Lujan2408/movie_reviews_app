from django.urls import path
from . import views

urlpatterns = [        
  path('signupaccount/', views.signupaccount, name='signupaccount'),
  path('logout/', views.logoutaccount, name='logout'),
  path('login/', views.loginaccount, name='loginaccount')
]