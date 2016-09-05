# -*- coding: utf-8 -*-
#coding=utf-8
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from utils.generator_util import random_str

def create_user_profile(sender, instance, created, **kwargs):  
    from .models import UserProfile
    if created:  
        profile, created = UserProfile.objects.get_or_create(user=instance,
                                                             headimg='android/headimg/default_head_185x185.jpg',
                                                             phone=random_str())  
  
post_save.connect(create_user_profile, sender=User) 

def create_profile_app(sender, instance, created, **kwargs):  
    from .models import UserApps
    if created:  
        apps, created = UserApps.objects.get_or_create(profile=instance,userid=instance.user.id,name=instance.user.username)  


