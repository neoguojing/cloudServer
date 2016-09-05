#coding=utf-8
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from app.models import *
from .controller import *
from .settings import DATA_NOEXIST,UER_NOLOGIN
from utils.download import *
import json

ANDROID_PROFILE = 1;
ANDROID_FRIEND = 2;
ANDROID_NEARBY = 3;
ANDROID_STATUS = 4;

HEADPIC = 1;
SIGNPIC =2;
STATUSPIC = 3;
USERPHOTO = 4;
ME = 5;

headpic_path = media_path+"android/headimg/"
signpic_path = media_path+"android/sign/"
statupic_path = media_path+"android/content_img/"
userphoto_path = media_path+"android/userphoto/"

def android_get_service(request,name, what):
    
    if not request.user.is_authenticated():
        return HttpResponse(UER_NOLOGIN,content_type="application/json")
        
    json_data =None;
    if  int(what)==ANDROID_PROFILE:
        json_data  = get_userprofile(name);
    elif  int(what)==ANDROID_FRIEND:
        json_data  = get_userfriend(name);
    elif  int(what)==ANDROID_NEARBY:
        json_data  = get_nearby(name);
    elif  int(what)==ANDROID_STATUS:
        json_data  = get_userstatus(name);
    elif  int(what)==ME:
        json_data  = get_me(name);
        
    if json_data==None:
        return HttpResponse(DATA_NOEXIST,content_type="application/json")

    return HttpResponse(json_data,content_type="application/json")
    
def android_get_without_login(request,name, what):
        
    json_data =None;
    if  int(what)==ANDROID_PROFILE:
        json_data  = get_userprofile(name);
    elif  int(what)==ANDROID_FRIEND:
        json_data  = get_userfriend(name);
    elif  int(what)==ANDROID_NEARBY:
        json_data  = get_nearby(name);
    elif  int(what)==ANDROID_STATUS:
        json_data  = get_userstatus(name);
    elif  int(what)==ME:
        json_data  = get_me(name);
        
    if json_data==None:
        return HttpResponse(DATA_NOEXIST,content_type="application/json")

    return HttpResponse(json_data,content_type="application/json")
    
def android_download(request,name, what):
    
    if not request.user.is_authenticated():
        return HttpResponse(UER_NOLOGIN,content_type="application/json")    
    
    userinfo  = (User.objects.filter(username=name));
    if (len(userinfo)==0):
        return HttpResponse(USER_NOEXIST,content_type="application/json")
        
    profile =  userinfo[0].userprofile;
    filepath = "";
    if  int(what)==HEADPIC:
        filepath  = headpic_path+profile.headimg.url.split("/")[-1];
        return image_download(request,filepath,name);
    elif  int(what)==SIGNPIC:
        filepath  = signpic_path+profile.getSignature().sign_pic.url.split("/")[-1];
    elif  int(what)==STATUSPIC:
        filepath  = signpic_path+profile.getSignature().sign_pic.url.split("/")[-1];
    elif  int(what)==ANDROID_STATUS:
        filepath  = signpic_path+profile.getSignature().sign_pic.url.split("/")[-1];
        
    if filepath=="":
        return HttpResponse(PIC_DOWNLOAD_ERROR,content_type="application/json")

    return fast_download(request,filepath,name);
    
def android_update_useraddr(request):
    ip = request.META['REMOTE_ADDR'];
    port = request.META['REMOTE_ADDR'];
    return HttpResponse(json.dumps(request),content_type="application/json");
    