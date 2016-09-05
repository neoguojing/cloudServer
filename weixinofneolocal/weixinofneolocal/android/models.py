#coding=utf-8  

from django.db import models


class MyApk(models.Model):
    name = models.CharField(max_length=255);
    apk = models.FileField(upload_to='android/apk');
    vandroid = models.CharField(max_length=255);
    version = models.IntegerField(default=0);
    description = models.TextField(blank=False);
    creaion_time = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str('%s' % (self.name))  
  
    def __unicode__(self):
        return u'%s %s' % (self.name, self.description) 
    
    class Meta:
        abstract = False
        app_label = 'android'
        ordering = ['-creaion_time']
        get_latest_by = ['-creaion_time']
        