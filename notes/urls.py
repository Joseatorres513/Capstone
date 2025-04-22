from django.urls import path
from . import views

urlpatterns = [
    path("list/", views.NoteListView.as_view(), name='notes_list'),
    path("create/", views.NotesCreate.as_view(), name='notes_create'),
]
