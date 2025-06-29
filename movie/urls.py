from django.urls import path
from . import views

urlpatterns = [
  # The path below is the PK for the movie represented as integer. Django adds an auto-increment PK in pur DB model under the hood
  path('<int:movie_id>', views.movie_detail, name='movie_detail'),
  path('<int:movie_id>/create', views.create_review, name="create_review"),
  path('review/<int:review_id>', views.updatereview, name='updatereview'),
  path('review/<int:review_id>/delete', views.deletereview, name='deletereview')
]