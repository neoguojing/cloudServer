# -*- coding: utf-8 -*-
import django
if django.VERSION < (1, 6):
    from django.conf.urls.defaults import *
else:
    from django.conf.urls import *


urlpatterns = patterns('forumapp.diamandas.userpanel.views',
    url(r'^$', 'user_panel'),
    url(r'^register/$', 'register'),
    url(r'^login/$', 'login_user'),
    url(r'^logout/$', 'logout_then_login'),
    url(r'^edit/$', 'edit_user_data'),
    url(r'^captcha/$', 'captchaRefresh'),
)
