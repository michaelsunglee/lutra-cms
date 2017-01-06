from django.db import models


class Note(models.Model):
    source_title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    page_number = models.IntegerField()
    date = models.DateTimeField('date added')
