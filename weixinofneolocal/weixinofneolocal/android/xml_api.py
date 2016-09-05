#coding=utf-8
import urllib2
import time
import random
from datetime import datetime

def calTime(lastlongin):
    return (lastlongin - datetime.now()).minutes;

def getPicName(picpath):
    return picpath.split("/")[-1]
    
def me_json(userprofile,state=0):
    if userprofile!=None:
        json_data = u''' 
        {"uid":%d,
        "avatar":"%s",
        "vip":%d,
        "group_role":%d,
        "industry":"%s",
        "weibo":%d,
        "tx_weibo":%d,
        "renren":%d,
        "device":%d,
        "relation":%d,
        "multipic":%d,
        "name":"%s",
        "gender":%d,
        "age":%d,
        "distance":"%s",
        "time":"%s",
        '''% (userprofile.user.id, userprofile.user.username,userprofile.vip, userprofile.grouprole,userprofile.industry,
              userprofile.userapps.sina,userprofile.userapps.weixin,userprofile.userapps.renren,userprofile.device,state,
              userprofile.multipic,userprofile.user.username,userprofile.gender,userprofile.getAge(),userprofile.getDistance(),
              userprofile.user.date_joined,)
        if userprofile.getlocation()!=None:
            json_data+='''
            "longitude":%f,
            "latitude":%f,
            '''% (userprofile.getlocation().longitude,userprofile.getlocation().latitude)
        else:
            json_data+='''
            "longitude":0,
            "latitude":0,
            '''
        if userprofile.getSignature()!=None:
            json_data+='''"sign":"%s",
            '''% (userprofile.getSignature().sign )
        else:
            json_data+='''"sign":"",'''
        
        json_data+='''"birthday":"%s"}''' % (userprofile.birthday)
        
    else:
        json_data = None;
    return json_data;

def profile_reply_json(user, userprofile, usersignature, userphotos):
    nums = len(userphotos);
    
    json_data = u"""
    {"uid":%d,
    "avatar":"%s",
    "name":"%s",
    "gender":%d,
    "age":%d,
    "constellation":"%s",
    "distance":"%s",
    "time":"%s",""" % (user.id, userprofile.user.username, user.username, 
                       userprofile.gender,userprofile.getAge(), 
                         userprofile.constellation, userprofile.getDistance(), user.date_joined)
    if usersignature!=None:
        json_data+=u"""
        "signature":
        {"sign":"%s",
        "sign_pic":"%s",
        "sign_dis":"%s"},
        """ % (usersignature.sign, usersignature.sign_pic.url.split("/")[-1] ,userprofile.getDistance())

    json_data+=u""""photos":
        [
        """
    if nums!=0:
        for num in range(0, nums):
            json_data+=u"""
            "%s"
            """% (userphotos[num].userphoto.url.split("/")[-1])   
            if num<(nums-1):
               json_data+=u''',''' 
    else:
        pass;
        
    json_data+=u"""]  }"""
    return json_data

def friend_reply_json(userrelation,state):
    nums = len(userrelation);
    
    if nums!=0:
        json_data = u'''
        ['''
        for num in range(0, nums):
            json_data += u''' 
            {"uid":%d,
            "avatar":"%s",
            "vip":%d,
            "group_role":%d,
            "industry":"%s",
            "weibo":%d,
            "tx_weibo":%d,
            "renren":%d,
            "device":%d,
            "relation":%d,
            "multipic":%d,
            "name":"%s",
            "gender":%d,
            "age":%d,
            "distance":"%s",
            "time":"%s",
            '''% (userrelation[num].user.id, userrelation[num].user.username,userrelation[num].vip, userrelation[num].grouprole,userrelation[num].industry,
                  userrelation[num].userapps.sina,userrelation[num].userapps.weixin,userrelation[num].userapps.renren,userrelation[num].device,state,
                  userrelation[num].multipic,userrelation[num].user.username,userrelation[num].gender,userrelation[num].getAge(),userrelation[num].getDistance(),
                  userrelation[num].user.date_joined,)
            if userrelation[num].getlocation()!=None:
                json_data+='''
                "longitude":%f,
                "latitude":%f,
                '''% (userrelation[num].getlocation().longitude,userrelation[num].getlocation().latitude)
            else:
                json_data+='''
                "longitude":0,
                "latitude":0,
                '''
            if userrelation[num].getSignature()!=None:
                json_data+='''"sign":"%s",
                '''% (userrelation[num].getSignature().sign )
            else:
                json_data+='''"sign":"",'''
            
            json_data+='''"birthday":"%s"}''' % (userrelation[num].birthday)
            if num<(nums-1):
                json_data+=''','''
            
        json_data += u''' ]'''
    else:
        json_data = None;
    return json_data;

def status_reply_json(userstatus):
    nums = len(userstatus);
    if nums!=0:
        json_data = u'''['''
        for num in range(0, nums):
            item ='''
           {"time":"%s",
            "content":"%s",
            "content_image":"%s",
            "site":"0",
            "comment_count":"%s"
            }
            '''% (userstatus[num].creaion_time, userstatus[num].content, userstatus[num].content_img.url.split("/")[-1], userstatus[num].content_count)
            if num<(nums-1):
                item+=''','''
            json_data+=item;
        json_data+=''']'''
    else:
        json_data = None;
    return json_data;

