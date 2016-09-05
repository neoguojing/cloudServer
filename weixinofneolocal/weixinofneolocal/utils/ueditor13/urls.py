# coding=utf-8
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
# Uncomment the next two lines to enable the admin:
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^static/', app.views),
    url(r'^image/', 'utils.ueditor13.views.imageUp'),
    url(r'^file/', 'utils.ueditor13.views.fileUp'),
    url(r'^scraw/', 'utils.ueditor13.views.scrawUp'),
    url(r'^video/', 'utils.ueditor13.views.videoUp'),
    url(r'^word/', 'utils.ueditor13.views.wordUp'),
    url(r'^screen/', 'utils.ueditor13.views.screenUp'),
    url(r'^imagemgnt/', 'utils.ueditor13.views.fileMgnt'),
    url(r'^catch/', 'utils.ueditor13.views.catchUp'),
    url(r'^onlion/', 'utils.ueditor13.views.videoOnlion'),

)
