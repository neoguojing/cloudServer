# coding=utf-8
from django.contrib import admin
from interface.models import *
from .models import *

class UserPhotosAdmin(admin.ModelAdmin):
    list_display = ('name', 'userid');
admin.site.register(UserPhotos, UserPhotosAdmin);
class UserLocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'userid');
admin.site.register(UserLocation,UserLocationAdmin);
class UserSignatureAdmin(admin.ModelAdmin):
    list_display = ('name', 'userid');
admin.site.register(UserSignature,UserSignatureAdmin);
class UserRelationAdmin(admin.ModelAdmin):
    list_display = ('name', 'userid')
admin.site.register(UserRelation,UserRelationAdmin);
class UserStatusAdmin(admin.ModelAdmin):
    list_display = ('name', 'userid')
admin.site.register(UserStatus,UserStatusAdmin);
class UserAppsAdmin(admin.ModelAdmin):
    list_display = ('name', 'userid')
admin.site.register(UserApps,UserAppsAdmin);
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone')
admin.site.register(UserProfile,UserProfileAdmin);

class WeiXinGroupsAdmin(admin.ModelAdmin):
    fields = (('gid', 'gname'), 'count');
    list_display = ('gid', 'gname', 'count');
admin.site.register(WeiXinGroups, WeiXinGroupsAdmin);

class WeiXinUsersAdmin(admin.ModelAdmin):
    fieldsets = (
                 (None, {
                        'fields':('userid', 'issubscribe', 'gid')
                 }),
    			(u'Basic info', {
                        'classes':('collapse',),
                        'fields':(('nickname', 'sex'), ('city', 'country', 'province'), 'language')
                 }),
    			(u'Others', {
                        'classes':('collapse',),
                        'fields':('headimgurl', ('subscribe_time', 'unionid'))
                 }),
    );
    list_display = ('nickname', 'issubscribe', 'gid');
admin.site.register(WeiXinUsers, WeiXinUsersAdmin);

class WeiXinDeveloperInfoAdmin(admin.ModelAdmin):
    fields = ('appid', 'secret', 'access_token', 'token', 'weixinid');
    list_display = ('appid', 'secret', 'access_token', 'token', 'weixinid');
admin.site.register(WeiXinDeveloperInfo, WeiXinDeveloperInfoAdmin);

class TextMsgAdmin(admin.ModelAdmin):
    fields = (('key', 'isactive'), 'text');
    list_display = ('key', 'key', 'text');
admin.site.register(TextMsg, TextMsgAdmin);

class MediaMsgAdmin(admin.ModelAdmin):
    fieldsets = (
    			(u'Basic info', {
                        'fields':(('key', 'userid'), ('msgtype', 'isactive'),)
                 }),
    			(u'Others', {
                        'classes':('collapse',),
                        'fields':('mediaid', 'filefd',)
                 }),
    );
    list_display = ('key', 'userid', 'msgtype', 'isactive');
admin.site.register(MediaMsg, MediaMsgAdmin);

class VideoMsgAdmin(admin.ModelAdmin):
    fieldsets = (
    			(u'Basic info', {
                        'fields':(('key', 'userid'), 'isactive')
                 }),
    			(u'Video info', {
                        'classes':('collapse',),
                        'fields':(('title', 'desc'), ('mediaid', 'filefd'))
                 }),
    );
    list_display = ('key', 'userid', 'isactive', 'title');
admin.site.register(VideoMsg, VideoMsgAdmin);

class MusicMsgAdmin(admin.ModelAdmin):
    fieldsets = (
    			(u'Basic info', {
                        'fields':(('key', 'userid'), 'isactive')
                 }),
    			(u'Video info', {
                        'classes':('collapse',),
                        'fields':(('title', 'desc'), ('url', 'hqurl'), ('mediaid', 'filefd'))
                 }),
    );
    list_display = ('key', 'userid', 'isactive', 'title');
admin.site.register(MusicMsg, MusicMsgAdmin);

class NewsAdmin(admin.ModelAdmin):
    fields = (('key', 'isactive'), 'itemcount');
    list_display = ('key', 'key', 'itemcount');
admin.site.register(News, NewsAdmin);

class ItemOfNewsAdmin(admin.ModelAdmin):
    fieldsets = (
    			(u'Basic info', {
                        'fields':('item', 'index',)
                 }),
    			(u'News info', {
                        'classes':('collapse',),
                        'fields':('title', 'description', 'pic_url', 'url')
                 }),
    );
    list_display = ('item', 'index', 'title');
admin.site.register(ItemOfNews, ItemOfNewsAdmin);

class LocationOfUserAdmin(admin.ModelAdmin):
    fieldsets = (
    			(u'Basic info', {
                        'fields':('msgtime', 'userid', 'msgid')
                 }),
    			(u'Location info', {
                        'classes':('collapse',),
                        'fields':(('latitude', 'longitude'), ('precision', 'scale'), 'lable')
                 }),
    );
    list_display = ('userid', 'msgtime',);
admin.site.register(LocationOfUser, LocationOfUserAdmin);

class MsgRecordAdmin(admin.ModelAdmin):
    fieldsets = (
    			(u'Basic info', {
                        'fields':(('msgid', 'msgtime'), 'userid')
                 }),
    			(u'Msg info', {
                        'classes':('collapse',),
                        'fields':(('msgtype', 'event'), 'eventkey',)
                 }),
    			(u'Others', {
                        'classes':('collapse',),
                        'fields':('title', 'content', 'url', 'mediaid', 'thumediaid', 'picount', 'picmd5')
                 }),
    );
    list_display = ('userid', 'msgtype', 'eventkey');
admin.site.register(MsgRecord, MsgRecordAdmin);

class ScanCodeAdmin(admin.ModelAdmin):
    fieldsets = (
    			(u'Msg info', {
                        'fields':('msgtime', ('userid', 'msgtype'), ('event', 'eventkey'))
                 }),
    			(u'Scan info', {
                        'classes':('collapse',),
                        'fields':(('scantype', 'scanresult'), 'tickit',)
                 }),
    );
    list_display = ('userid', 'msgtime', 'msgtype');
admin.site.register(ScanCode, ScanCodeAdmin);
