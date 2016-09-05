# -*- coding: utf-8 -*-
#coding=utf-8
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.contrib import auth
from app.models import *
from ..controller import *
from ..settings import  *
import json

@csrf_exempt   
def islogin(request):
    if not request.user.is_authenticated():
        return HttpResponse(UER_NOLOGIN,content_type="application/json")
    else:
        return HttpResponse(LOGIN_SUCCESS,content_type="application/json");

def _login_check(request,username,password):
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        # Correct password, and the user is marked "active"
        auth.login(request, user);
        return HttpResponse(LOGIN_SUCCESS,content_type="application/json");
    else:
        return HttpResponse(PASSWORD_INVALICE,content_type="application/json");

@csrf_exempt   
def user_login(request):
    if request.method == 'POST':
        loginfo = json.loads(request.body);
        if len(loginfo.keys())==0:
            return HttpResponse(INVALIDE_JSON,content_type="application/json")
        
        username = loginfo.get('username','');
        password = loginfo.get('password', '');
        
        if password=='':
            return HttpResponse(PASSWORD_ISNONE,content_type="application/json");
            
        if username!='':
            uset = User.objects.filter(username=username);
            if len(uset)==0:
                return HttpResponse(USER_NOEXIST,content_type="application/json");
                
            return _login_check(request,username,password);
        
        phone = loginfo.get('phone','');
        if phone!='':
            phnum = UserProfile.objects.filter(phone=phone);
            if len(phnum)!=0:
                username = phnum[0].user.username;
                return _login_check(request,username,password);
            else:
                return HttpResponse(PHONE_NOEXIST,content_type="application/json")
                
        email = loginfo.get('email','');
        if email!='':
            emailset = User.objects.filter(email=email);
            if len(emailset)!=0:
                username = emailset[0].username;
                return _login_check(request,username,password);
            else:
                return HttpResponse(EMAIL_NOEXIST,content_type="application/json")
            
    return HttpResponse(INVALIDE_JSON,content_type="application/json")

@csrf_exempt  
def user_login_post(request):
    if request.method == 'POST':
        loginfo = request.POST;
        username = loginfo.get('username','');
        password = loginfo.get('password', '');
        
        if password=='':
            return HttpResponse(PASSWORD_ISNONE,content_type="application/json");
            
        if username!='':
            uset = User.objects.filter(username=username);
            if len(uset)==0:
                return HttpResponse(USER_NOEXIST,content_type="application/json");
                
            return _login_check(request,username,password);
            
    return HttpResponse(INVALIDE_JSON,content_type="application/json")

def user_logout(request):
    if not request.user.is_authenticated():
        return HttpResponse(UER_NOLOGIN,content_type="application/json")
        
    auth.logout(request);
    return HttpResponse(UERE_LOGOUT,content_type="application/json");
    
def user_init(request):
    if not request.user.is_authenticated():
        return HttpResponse(UER_NOLOGIN,content_type="application/json")
        
    response = HttpResponse(content_type="application/json");
    response['profile']=get_userprofile(request.user.id);
    response['status']=get_userstatus(request.user.id);
    response['friends']=get_userfriend(request.user.id);
    response['nearby']=get_nearby(request.user.id);
    return response;