from django.db import models
from django.core.urlresolvers import reverse


class Album(models.Model):
    place = models.CharField(max_length=140)
    album_cover = models.FileField()

    def get_absolute_url(self):
        return reverse('index')

    def __str__(self):
        return self.place


class Journal(models.Model):
    journal = models.ForeignKey(Album, on_delete=models.CASCADE)
    journal_title = models.CharField(max_length=140, blank=True)
    journal_details = models.TextField()
    date = models.CharField(max_length=100, default='')
    time = models.CharField(max_length=10, default='')
    journal_image = models.FileField(blank=True)

    def get_absolute_url(self):
        return reverse('index')

    def __str__(self):
        return self.journal_title
