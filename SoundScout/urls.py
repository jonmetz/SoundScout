from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', 'SoundScout.views.index', name='index'),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^songs/', include('songs.urls')),
                       url(r'^search/', include('search.urls')),                       
                       url(r'^browse/', 'SoundScout.views.browse', name='browse'),
                       url(r'^about/', 'SoundScout.views.about', name='about'),        
                       url(r'^contact/', 'SoundScout.views.contact', name='contact'),            
                       url(r'^legal/', 'SoundScout.views.legal', name='legal'),
)

                    

                           

