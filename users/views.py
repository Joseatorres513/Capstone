from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView

# Create your views here.
class UserLogin(LoginView):
    template_name = "users/login.html"

    def get_success_url(self):
        return reverse('home')