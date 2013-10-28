from django.conf.urls import patterns, include, url
from search import views

urlpatterns = patterns('',
                       url(r'^$', views.searchpage, name='searchpage'),
                       url(r'^form.html?q=[\w|\s]+$', views.searchform, name='searchform'),
                       url(r'^form.html$', views.searchform, name='searchform'),
                       url(r'^(?P<search_query>[\w|\s]+)/$', views.results, name='results_page'),
                       url(r'^looked_for/(?P<search_query>[\w|\s]+)/$', views.looked_for, name='looked_for'),
                       
)
