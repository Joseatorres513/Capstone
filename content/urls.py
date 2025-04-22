from django.urls import path
from . import views

urlpatterns = [
    path("", views.projects_list_view, name="projects_list"),
    path("new/", views.project_new_view, name="project_new"),
    path("delete/<int:pk>/", views.project_delete, name="project_delete"),
    path("update/<int:pk>/", views.project_update, name="project_update"),  # <-- This line fixes your error
]