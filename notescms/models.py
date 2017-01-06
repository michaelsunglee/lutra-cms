from django.db import models


class Note(models.Model):
    source_title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    note = models.TextField()
    page_number = models.IntegerField()
    date = models.DateTimeField('date added')

    def __str__(self):
        return "{} by {} in {}".format(self.note, self.author, self.source_title)
