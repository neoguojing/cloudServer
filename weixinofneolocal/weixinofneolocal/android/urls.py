# -*- coding: utf-8 -*-
#coding=utf-8
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
# Uncomment the next two lines to enable the admin:

from config import settings
admin.autodiscover()

urlpatterns = patterns('android.views',
                       
    url(r'^download/(?P<name>[a-zA-Z0-9_-]+)/(?P<what>[0-9]+)/$', 'android_download'),
    url(r'^get/(?P<name>[a-zA-Z0-9_-]+)/(?P<what>[0-9]+)/$', 'android_get_service'),
    url(r'^getwithoutlogin/(?P<name>[a-zA-Z0-9_-]+)/(?P<what>[0-9]+)/$', 'android_get_without_login'),
    url(r'^getuseraddr/$', 'android_update_useraddr'),
)+ static(settings.STATIC_URL, document_root=settings.APP_STATIC)

urlpatterns += patterns('android.register.views',
                       
    url(r'^register/$', 'user_register'),
    url(r'^headpic/$', 'headpic_upload'),

)+ static(settings.STATIC_URL, document_root=settings.APP_STATIC)

urlpatterns += patterns('android.login.views',
                       
    url(r'^login/$', 'user_login'),
    url(r'^logincheck/$', 'islogin'),
    url(r'^loginpost/$', 'user_login_post'),
    url(r'^logout/$', 'user_logout'),

)+ static(settings.STATIC_URL, document_root=settings.APP_STATIC)

urlpatterns += patterns('android.apkdld.views',
                       
    url(r'^getapk/(?P<name>[a-zA-Z0-9_-]+)/(?P<version>[0-9]+)/$', 'apk_download',name="downloadapk"),
    url(r'^getapk/$', 'apk_list',name="getapklist"),

)+ static(settings.STATIC_URL, document_root=settings.APP_STATIC)

urlpatterns += patterns('android.login.test',
                       
    url(r'^logintest/$', 'user_login_test'),
    url(r'^logouttest/$', 'user_logout_test'),

)+ static(settings.STATIC_URL, document_root=settings.APP_STATIC)

urlpatterns += patterns('android.register.test',
                       
    url(r'^registertest/$', 'register_test'),

)+ static(settings.STATIC_URL, document_root=settings.APP_STATIC)