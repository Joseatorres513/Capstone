from django.shortcuts import render
from django.views.generic import ListView
from .models import Note

"""
Class-based views:
Views           = generic views
ListView      = get a list of records
DetiailView   = get a single record
CreateView   = create a new record
DeleteView   = delete a record
UpdateView   = modify an existing record
LoginView   = login a user
"""

# Create your views here.
# def list(request):
#    return render(request, 'notes/list.html')


class NoteListView(ListView):
    model = Note
    template_name = 'notes/list.html'
    context_object_name = 'all_notes'
