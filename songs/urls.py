from django.conf.urls import patterns, include, url

from songs import views

urlpatterns = patterns('',
                       url(r'^(?P<song_id>\d+)/$', views.song, name='song'),
)

