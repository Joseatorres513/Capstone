from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_view, name="home"),                     # Home Page
    path("about/", views.about_view, name="about"),             # About Page
    path("experience/", views.experience_view, name="experience"),  # Experience Page
    path("contact/", views.contact_view, name="contact"),       # Contact form submission (POST)
    path("contact_form/", views.contact_form_view, name="contact_form"),  # Optional form renderer
    path("testing_page/", views.testing_view, name="testing_page"),  # Dev/testing route
]