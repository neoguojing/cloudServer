# coding=utf-8
from django.db import models

class WeiXinGroups(models.Model):
    gid = models.IntegerField(primary_key=True)
    gname = models.CharField(max_length=30, blank=True)
    count = models.IntegerField(blank=True)
    def __unicode__(self):
        return "%s" % (self.gname)

class WeiXinUsers(models.Model):
    # userid = models.CharField(max_length=50)
    userid = models.CharField(primary_key=True, max_length=50)
    issubscribe = models.BooleanField()
    gid = models.ForeignKey(WeiXinGroups, related_name='user_set') 
    # gid = models.IntegerField() 
    nickname = models.CharField(max_length=30, blank=True)
    sex = models.BooleanField()
    city = models.CharField(max_length=30, blank=True)
    country = models.CharField(max_length=30, blank=True)
    province = models.CharField(max_length=30, blank=True)
    language = models.CharField(max_length=10, blank=True)
    headimgurl = models.URLField(blank=True)
    subscribe_time = models.IntegerField(blank=True)
    unionid = models.CharField(max_length=50, blank=True)
    
    def __unicode__(self):
        return "%s %s %s %s %s" % (self.nickname, self.city, self.country, \
        self.province, self.userid)
    
    class Meta:
        ordering = ['gid', 'nickname']

class WeiXinDeveloperInfo(models.Model):
    appid = models.CharField(max_length=30)
    secret = models.CharField(max_length=50)
    access_token = models.CharField(max_length=50, blank=True)
    token = models.CharField(max_length=10)
    weixinid = models.CharField(max_length=30)

    def __unicode__(self):
        return "%s %s %s" % (self.appid, self.token, self.weixinid)
###############################################################################
        
class TextMsg(models.Model):
    key = models.CharField(max_length=30)
    isactive = models.BooleanField();
    text = models.TextField(blank=True)
    
    def __unicode__(self):
        return "%s %s" % (self.key, self.text)
# voice image
class MediaMsg(models.Model):
    key = models.CharField(max_length=30)
    userid = models.ForeignKey(WeiXinUsers);
    msgtype = models.CharField(max_length=10)
    isactive = models.BooleanField();
    mediaid = models.CharField(max_length=200)
    # filefd = models.FileField(upload_to='image/')
    filefd = models.TextField()
    
    def __unicode__(self):
        return "%s %s" % (self.key, self.msgtype)

class VideoMsg(models.Model):
    key = models.CharField(max_length=30)
    userid = models.ForeignKey(WeiXinUsers);
    isactive = models.BooleanField();
    title = models.CharField(max_length=50, blank=True)
    desc = models.TextField(blank=True)
    mediaid = models.CharField(max_length=200)
    filefd = models.FileField(upload_to='video/')
    
    def __unicode__(self):
        return "%s %s %s" % (self.key, self.title, self.desc)

class MusicMsg(models.Model):
    key = models.CharField(max_length=30)
    userid = models.ForeignKey(WeiXinUsers);
    isactive = models.BooleanField();
    title = models.CharField(max_length=50, blank=True)
    desc = models.TextField(blank=True)
    url = models.URLField(blank=True)
    hqurl = models.URLField(blank=True)
    mediaid = models.CharField(max_length=200)
    filefd = models.FileField(upload_to='music/')
    
    def __unicode__(self):
        return "%s %s %s" % (self.key, self.title, self.desc)

# 用于图文回复的
class News(models.Model):
    key = models.CharField(max_length=30, primary_key=True)
    isactive = models.BooleanField();
    itemcount = models.IntegerField() 
    
    def __unicode__(self):
        return "%s" % (self.key)

class ItemOfNews(models.Model):
    item = models.ForeignKey(News, related_name='item_set') 
    # item = models.CharField(max_length=30)
    index = models.IntegerField()
    title = models.CharField(max_length=50, blank=True)
    description = models.TextField(blank=True)
    # 图片链接，支持JPG、PNG格式，较好的效果为大图360*200，小图200*200
    pic_url = models.URLField(blank=True)
    # 点击图文消息跳转链接
    url = models.URLField(blank=True)

    def __unicode__(self):
        return "%s %s" % (self.title, self.description)
   # 认认排序方式
    class Meta:
        verbose_name_plural = "item"

class LocationOfUser(models.Model):
    msgtime = models.IntegerField(primary_key=True);
    userid = models.ForeignKey(WeiXinUsers);
    msgid = models.BigIntegerField(blank=True, default=0);
    latitude = models.FloatField();
    longitude = models.FloatField();
    precision = models.FloatField(blank=True, default=0.0);
    scale = models.IntegerField(blank=True, default=0);
    lable = models.CharField(max_length=100, blank=True);
    
    def __unicode__(self):
        return "%s %s" % (self.userid, self.lable);
    class Meta:
        ordering = ['userid', 'msgtime']
# except voice, scancer,button event
class MsgRecord(models.Model):
    msgid = models.BigIntegerField(default=0);
    msgtime = models.IntegerField(primary_key=True);
    userid = models.ForeignKey(WeiXinUsers);
    msgtype = models.CharField(max_length=30);
    event = models.CharField(max_length=30, blank=True, default='');
    eventkey = models.CharField(max_length=50, blank=True);
    title = models.CharField(max_length=50, blank=True);
    content = models.TextField(blank=True);
    url = models.URLField(blank=True);
    mediaid = models.CharField(max_length=200);
    thumediaid = models.CharField(max_length=200);
    picount = models.IntegerField(default=0);
    picmd5 = models.CharField(max_length=50, blank=True, default='');
    
    class Meta:
        ordering = ['userid', 'msgtime']
    
    def __unicode__(self):
        return "%s %s %s" % (self.userid, self.title, self.content);
    
class ScanCode(models.Model):
    msgtime = models.IntegerField(primary_key=True);
    userid = models.ForeignKey(WeiXinUsers);
    msgtype = models.CharField(max_length=30, blank=True, default='');
    event = models.CharField(max_length=30, blank=True, default='');
    eventkey = models.CharField(max_length=50, blank=True, default='');
    scantype = models.CharField(max_length=30, blank=True, default='');
    scanresult = models.CharField(max_length=200, blank=True, default='');
    tickit = models.CharField(max_length=100, blank=True, default='');

    class Meta:
        ordering = ['userid', 'msgtime']
    
    def __unicode__(self):
        return "%s" % (self.userid);
'''
class Reply(models.Model):
    reply_type_choice = (("text", "Text"), ("voice", "Voice"), ("video", "Video"), ("news", "Multi pics"), ("music", "Music"), ("action", "Action"), )
    reply_type = models.CharField(max_length=10, choices=reply_type_choice)
    #下面用于纯文本回复
    text_reply = models.TextField(blank=True)
    #下面用于voice回复
    voice_reply = models.TextField(blank=True)
    #下面用于video回复
    video_reply = models.TextField(blank=True)
    #下面的用于图文回复
    news_reply = models.ManyToManyField(News, blank=True)
    #下面是回复音乐
    music_title = models.CharField(max_length=40, blank=True)
    music_description = models.CharField(max_length=40, blank=True)
    music_url = models.URLField(blank=True)
    music_hq_url = models.URLField(blank=True)
    #下面是使用action回复的
    action = models.CharField(max_length=30, blank=True)
    parameter = models.CharField(max_length=20, blank=True)

    def __unicode__(self):
        return "%s" % (self.reply_type, )


class Keyword(models.Model):
    keyword = models.CharField(max_length=20)
    reply = models.ForeignKey(Reply)

    def __unicode__(self):
        return "%s %s" % (self.keyword, self.reply)
'''
