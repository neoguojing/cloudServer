# -*- coding: utf-8 -*-
# coding=utf-8
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
# Uncomment the next two lines to enable the admin:

from config import settings
admin.autodiscover()

urlpatterns = patterns('app.views',
    # Examples:

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^static/', app.views),
    # url(r'^admin/', include(admin.site.urls)),
    # url(r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.APP_STATIC}),

    url(r'^news/(?P<key>[a-zA-Z0-9_-]+)/$', 'WeixinNews'),
    url(r'^news/(?P<key>[a-zA-Z0-9_-]+)/(?P<index>[0-9]+)/$', 'WeixinNews'),
    url(r'^bootstrap/$', 'BootstrapTest'),
    url(r'^init/$', 'SysInit'),
    url(r'^$', 'AppMain'),

) + static(settings.STATIC_URL, document_root=settings.APP_STATIC)

urlpatterns += patterns('utils.download',
    url(r'download/(?P<fileaname>[a-zA-Z0-9_-]+)/$', 'fast_download'),
    url(r'download1/(?P<the_file_name>[a-zA-Z0-9_-]+)/$', 'big_file_download'),
    url(r'download2/(?P<filepath>[a-zA-Z0-9_-]+)/$', 'big_file_download1'),
    url(r'zipdld/(?P<filepath>[a-zA-Z0-9_-]+)/$', 'zip_file_download'),
)


urlpatterns += patterns('app.ajax',
    url(r'captcha1/', 'calcuteVertifyCode1'),
    url(r'captcha/', 'calcuteVertifyCode'),
    url(r'test/', 'multiply1'),
)
