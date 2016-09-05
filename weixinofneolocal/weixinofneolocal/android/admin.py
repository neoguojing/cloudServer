# coding=utf-8
from django.contrib import admin
from .models import *

class MyApkAdmin(admin.ModelAdmin):
    list_display = ('name', 'version', 'creaion_time');
admin.site.register(MyApk, MyApkAdmin);
