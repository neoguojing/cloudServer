# -*- coding: utf-8 -*-
#coding=utf-8
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from app.models import *
from ..controller import *
from ..settings import  *
import json
from interface.utils import *

util = WeixinUtil();

def _login_check(request,username,password):
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        # Correct password, and the user is marked "active"
        auth.login(request, user);
        return HttpResponse(LOGIN_SUCCESS,content_type="application/json");
    else:
        return HttpResponse(PASSWORD_INVALICE,content_type="application/json");
    
def user_login_test(request):
    data = util.method_postjson_api("http://101.88.15.37:10000/site1/android/login/",login_json);
    return HttpResponse(json.dumps(data),content_type="application/json")
    
def user_logout_test(request):
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