from django.urls import path
from . import views

urlpatterns = [
    path('articles/', views.article_list), # 이제 앱 네임 필요없음
    path('articles/<int:article_pk>/', views.article_detail),
    path('comments/', views.comment_list),
    path('comments/<int:comment_pk>/', views.comment_detail),
    path('articles/<int:article_pk>/comments/', views.comment_create),
]