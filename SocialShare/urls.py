from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('insta_com/', views.insta_com, name='insta_com'),
    path('insta_msg/', views.insta_msg, name='insta_msg'),
    path('fb_com/', views.fb_com, name='fb_com'),
    path('fb_msg/', views.fb_msg, name='fb_msg'),
    path('fb_post/', views.fb_post, name='fb_post'),
    path('li_com/', views.li_com, name='li_com'),
    path('li_post/', views.li_post, name='li_post'),
    path('twitter_com/', views.twitter_com, name='twitter_com'),
    path('twitter_post/', views.twitter_post, name='twitter_post'),
    path('quora_com/', views.quora_com, name='quora_com'),
    path('quora_post/', views.quora_post, name='quora_post'),
    path('reddit_com/', views.reddit_com, name='reddit_com'),
    path('reddit_post/', views.reddit_post, name='reddit_post'),
    path('disqus_com/', views.disqus_com, name='disqus_com'),
]