import django_tables2 as tables
from .models import Note


class NoteTable(tables.Table):
    class Meta:
        model = Note
        template = 'django_tables2/bootstrap.html'
        attrs = {'class': 'table table-bordered table-striped table-hover'}
