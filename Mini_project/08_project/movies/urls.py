from django.urls import path
from . import views

urlpatterns = [
    path('movies/', views.movie_list),
    path('movies/<int:movie_pk>/', views.movie_detail),
    path('movies/<int:movie_pk>/reviews/', views.review_list),
    path('movies/<int:movie_pk>/reviews/<int:review_pk>/', views.reivew_detail),
    path('movies/<int:movie_pk>/reviews/<int:review_pk>/comments/', views.comment_create),
]
