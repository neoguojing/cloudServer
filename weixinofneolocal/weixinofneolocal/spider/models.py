#coding=utf-8  
#!/usr/bin/python
# -*- coding: utf-8 -*-

from datetime import datetime

from django.db import models
from django.utils.translation import ugettext as _
from django.contrib.auth.models import User
from .signals import *  

class UserProfileManager(models.Manager):
    #def get_query_set(self):
     #   return super(ServerViewManager, self).get_query_set().filter(name='neo').latest('creaion_time')
    
    def getSignature(self, uid):
        try:
            record = self.sign_set.latest('creaion_time');
        except Exception,e: 
            record = None;
        finally:
            return record;
        
    def getFriendsSet(self, uname):
        objlist = [];
        try:
            record = self.frd_set.filter(relation=1);
            for obj in record:
                profile =  (User.objects.filter(id=obj.frendid))[0].userprofile;
                objlist.append(profile);
        except Exception,e: 
            objlist = [];
        finally:
            return objlist;
        
    def getNearBy(self, uname):
        objlist = [];
        try:
            record = self.frd_set.filter(relation=0);
            for obj in record:
                profile =  (User.objects.filter(id=obj.frendid))[0].userprofile;
                objlist.append(profile);
        except Exception,e: 
            objlist = [];
        finally:
            return objlist;
    

class UserProfile(models.Model):
    """
    User Profile for platform
    """
    '''白羊座[Aries] 金牛座[Taurus]双子座[Gemini]巨蟹座[Cancer]狮子座[Leo]处女座[Virgo]天秤座[Libra]天蝎座[Scorpius]射手座[Sagittarius]
    摩羯座[Capricorn]水瓶座[Aquarius]双鱼座[Pisces]'''
    CONSTELLATION_CHOICES= (
                            (u'白羊座',u'白羊座'),
                            (u'金牛座',u'金牛座'),
                            (u'双子座',u'双子座'),
                            (u'巨蟹座',u'巨蟹座'),
                            (u'狮子座',u'狮子座'),
                            (u'处女座',u'处女座'),
                            (u'天秤座',u'天秤座'),
                            (u'天蝎座',u'天蝎座'),
                            (u'射手座',u'射手座'),
                            (u'摩羯座',u'摩羯座'),
                            (u'水瓶座',u'水瓶座'),
                            (u'双鱼座',u'双鱼座')
                                                            )
    user = models.OneToOneField(User)
    SEX_CHOICES= ((0,'Female'),(1,'Male'))
    gender = models.BooleanField(choices=SEX_CHOICES, default=1);
    headimg = models.ImageField(upload_to='android/headimg', blank=True);
    birthday = models.DateField(blank=True,default=datetime.now().date());
    constellation = models.CharField(blank=True, max_length=255,choices=CONSTELLATION_CHOICES,null = True );
    phone = models.CharField(blank=True, max_length=20,unique=True);
    vip = models.BooleanField(default=0);
    grouprole = models.IntegerField(default=0);
    industry = models.CharField(blank=True, max_length=255);
    DEVICE_CHOICES= ((0,'android'),(1,'iphone'))
    device = models.IntegerField(choices=DEVICE_CHOICES, default=0);
    multipic = models.BooleanField(default=0);
    
    
    detail = UserProfileManager();
    objects = models.Manager();
    
    def __str__(self):
        return str('%s %s' % (self.constellation, self.industry))  
  
    def __unicode__(self):
        return u'%s %s' % (self.constellation, self.industry) 
    
    def getAge(self):
        if self.birthday:
            return ((datetime.now().date() - self.birthday).days)/365;
        return 0;
    
    def getDistance(self):
        return None;
    
    def getSignature(self,):
        try:
            record = self.sign_set.latest('creaion_time');
        except Exception,e: 
            record = None;
        finally:
            return record;
        
    def getlocation(self,):
        try:
            record = self.loca_set.latest('creaion_time');
        except Exception,e: 
            record = None;
        finally:
            return record;
        
    def getFriendsSet(self):
        objlist = [];
        try:
            record = self.frd_set.filter(relation=1);
            for obj in record:
                profile =  (User.objects.filter(id=obj.frendid))[0].userprofile;
                objlist.append(profile);
        except Exception,e: 
            objlist = [];
        finally:
            return objlist;
        
    def getNearBy(self):
        objlist = [];
        try:
            record = self.frd_set.filter(relation=0);
            for obj in record:
                profile =  (User.objects.filter(id=obj.frendid))[0].userprofile;
                objlist.append(profile);
        except Exception,e: 
            objlist = [];
        finally:
            return objlist;
     #pk = primary key
    '''def save(self, **kwargs):
        if self.pk:
            if not self.last_visit:
                self.last_visit = datetime.now()
                self.last_visit = self.onsitedata
                self.onsitedata = datetime.now()
            super(UserProfile, self).save(**kwargs)'''
        
post_save.connect(create_profile_app, sender=UserProfile) 

class UserPhotos(models.Model):
    name = models.CharField(blank=False, max_length=255);
    userid = models.IntegerField(blank=False);
    userphoto = models.ImageField(upload_to='android/userphoto');
    info = models.CharField(blank=True, max_length=255);
    profile = models.ForeignKey(UserProfile,related_name='pic_set');
    creaion_time = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = False
        app_label = 'app'
        ordering = ['-creaion_time']
        get_latest_by = ['-creaion_time']
        
    '''def save(self, **kwargs):
        if self.userid:
            (User.objects.filter(id=self.userid))[0].userprofle.pic_set.add(self);
            super(UserPhotos, self).save(**kwargs);'''

class UserLocation(models.Model):
    name = models.CharField(blank=False, max_length=255);
    userid = models.IntegerField(blank=False);
    #latitude = models.FloatField(max_digits=8, decimal_places=3);
    #longitude = models.FloatField(max_digits=8, decimal_places=3);
    latitude = models.FloatField(blank=False);
    longitude = models.FloatField(blank=False);
    info = models.CharField(blank=True, max_length=255,null=True);
    profile = models.ForeignKey(UserProfile,related_name='loca_set');
    creaion_time = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = False
        app_label = 'app'
        ordering = ['-creaion_time']
        get_latest_by = ['-creaion_time']
        
        
class UserSignature(models.Model):
    name = models.CharField(max_length=255,blank=False);
    userid = models.IntegerField(blank=False);
    sign = models.TextField(blank=False);
    sign_pic = models.ImageField(upload_to='android/sign');
    profile = models.ForeignKey(UserProfile,related_name='sign_set');
    creaion_time = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = False
        app_label = 'app'
        ordering = ['-creaion_time']
        get_latest_by = ['-creaion_time']
        
    
class UserRelation(models.Model):
    RELATION_CHOICES= ((0,'stranger'),(1,'friend'))
    name = models.CharField( max_length=255,blank=False);
    userid = models.IntegerField(blank=False);
    frendid = models.IntegerField(blank=False);
    relation = models.IntegerField(default=0,choices=RELATION_CHOICES);
    profile = models.ForeignKey(UserProfile,related_name='frd_set');
    
    
class UserStatus(models.Model):
    name = models.CharField(max_length=255,blank=False);
    userid = models.IntegerField(blank=False);
    creaion_time = models.DateTimeField(auto_now=True);
    content = models.TextField(blank=False);
    content_img = models.ImageField(upload_to='android/content_img',blank=True);
    content_count = models.IntegerField(default=0);
    location  = models.OneToOneField(UserLocation);
    profile = models.ForeignKey(UserProfile,related_name='statu_set');
    
    class Meta:
        abstract = False
        app_label = 'app'
        ordering = ['-creaion_time']
        get_latest_by = ['-creaion_time']
    
class UserApps(models.Model):
    profile = models.OneToOneField(UserProfile);
    name = models.CharField(unique=True, max_length=255,blank=False);
    userid = models.IntegerField(unique=True,blank=False);
    sina = models.BooleanField(default=0);
    weixin = models.BooleanField(default=0);
    renren = models.BooleanField(default=0);
    fb = models.BooleanField(default=0);
    google = models.BooleanField(default=0);
    twitter = models.BooleanField(default=0);
    
    

