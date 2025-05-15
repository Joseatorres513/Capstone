from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_home, name='blog_home'),
    path('posts/', views.blog_posts, name='blog_posts'),
    path('contact/', views.blog_contact, name='blog_contact'),
]
