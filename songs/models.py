from django.db import models

class Song(models.Model):

    def __unicode__(self):
        return self.title

    title = models.CharField(max_length=40)
    artist = models.CharField(max_length=40)
    artwork = models.URLField()
    url = models.URLField()
    #downloads = models.
    #size = models.length(max_length=5)
    #bitrate =     
    

