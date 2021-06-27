from django.urls import path
from . import views

app_name = 'community'

urlpatterns = [
    path('reviews/', views.index, name='index'),
    path('reviews/create/', views.create, name='create'),
    path('reviews/<int:review_pk>/', views.detail, name='detail'),
    path('reviews/<int:review_pk>/comments/',
         views.create_comment, name='create_comment'),
    path('reviews/<int:review_pk>/like/', views.like, name='like'),
]
