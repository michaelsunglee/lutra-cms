import django_tables2 as tables
from .models import Note


class NoteTable(tables.Table):
    class Meta:
        model = Note
