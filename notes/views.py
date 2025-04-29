from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Note, NoteComment
from django.urls import reverse_lazy
from .forms import NoteForm

"""
Class-based views:
Views           = generic views
ListView      = get a list of records
DetailView   = get a single record
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

class NotesCreateView(CreateView):
    model = Note
    form_class = NoteForm
    template_name = 'notes/create.html'
    success_url = reverse_lazy('notes_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form_title"] = "Create New Note"
        return context
    
class NoteDetailView(DetailView):
    model = Note
    template_name = 'notes/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ["comments"] = NoteComment.objects.filter(note=self.object).order_by("-created_on")

class NoteUpdateView(UpdateView):
    model = Note
    template_name = 'notes/create.html'
    form_class = NoteForm
    success_url = reverse_lazy('notes_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form_title"] = "Update Note"
        return context

class NoteDeleteView(DeleteView):
    model = Note
    template_name = 'notes/delete.html'
    success_url = reverse_lazy('notes_list')


def create_comment(request):
    content = request.POST.get('content')
    note_id = request.POST.get('note_id')
    user = request.user

    note = Note.objects.get(id=note_id)

    comment = NoteComment.objects.create(
        note = note,
        content = content,
        author = user
    )

    comment.save()

    return redirect('notes_detail', pk=note_id)