from django.shortcuts import render
from django.views import generic
from .models import Note


class NotesView(generic.ListView):
    template_name = 'notescms/index.html'
    context_object_name = 'notes_list'

    def get_queryset(self):
        return Note.objects.all()
