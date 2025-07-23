from django.urls import path
from .views import news_list

urlpatterns = [
    path('news/', news_list, name='news_list'),
    path('articles/', article_list, name='article_list'),
    path('news/<int:pk>/', post_detail, name='post_detail'),
]
