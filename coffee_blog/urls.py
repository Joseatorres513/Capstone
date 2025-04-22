from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='coffee_home'),
    path('about/', views.about, name='coffee_about'),
    path('contact/', views.contact, name='coffee_contact'),
    path('courses/', views.courses, name='coffee_courses'),
]
