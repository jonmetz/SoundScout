from django.db import models


class Song(models.Model):
    title = models.CharField(max_length=40)
    artist = models.CharField(max_length=40)
    artwork = models.URLField()
    #size = models.length(max_length=5)
    #bitrate = 
    url = models.URLField()
    downloads =

