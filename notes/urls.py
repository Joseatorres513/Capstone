from django.urls import path
from . import views

urlpatterns = [
    path("list/", views.NoteListView.as_view(), name='notes_list'),
    path("create/", views.NotesCreateView.as_view(), name='notes_create'),
    path("details/<int:pk>/", views.NoteDetailView.as_view(), name='notes_detail'),
    path("update/<int:pk>/", views.NoteUpdateView.as_view(), name='notes_update'),
    path("delete/<int:pk>/", views.NoteDeleteView.as_view(), name='notes_delete'),
]
