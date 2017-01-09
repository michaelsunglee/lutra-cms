from django.shortcuts import render
from django.views import generic
from .models import Note
from .tables import NoteTable


class NotesView(generic.ListView):
    template_name = 'notescms/index.html'
    context_object_name = 'notes_table'

    def get_queryset(self):
        table = NoteTable(Note.objects.all())
        return table
