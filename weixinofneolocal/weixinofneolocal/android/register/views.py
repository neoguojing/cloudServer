#coding=utf-8
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from app.models import *
from ..controller import *
from ..settings import  *
from utils.generator_util import random_vericode

def _phone_check(phonenum):
    if len(UserProfile.objects.filter(phone=phonenum))==0:
        return True;
    return False;
    
def _username_check(name):
    if len(User.objects.filter(username=name))==0:
        return True;
    return False;

@csrf_exempt
def headpic_upload(request):
    if request.method == 'POST':
        if request.FILES.get('headpic','')!='':
            headpic = request.FILES.get('headpic');
            if update_headpic(request.POST.get("username"),headpic):
                return HttpResponse(NOERROR,content_type="application/json")
            else:
                return HttpResponse(USER_NOEXIST,content_type="application/json")
        return HttpResponse(PIC_UPLOAD_FAILED,content_type="application/json");
        
@csrf_exempt
def user_register(request):
    if request.method == 'POST':
        reginfo = json.loads(request.body);
        if len(reginfo.keys())==0:
            return HttpResponse(INVALIDE_JSON,content_type="application/json")
            
        step = reginfo.get('step','');
        
        if step!='':
            if step=='1':
                phone = reginfo.get('phone','');
                if phone!='':
                    if _phone_check(phone):
                        return HttpResponse(NOERROR,content_type="application/json")
                    else:
                        return HttpResponse(PHONE_REGISTERED,content_type="application/json")
            elif step=='2':
                code_json = get_verify_json(random_vericode());
                return HttpResponse(code_json,content_type="application/json")
            elif step=='3':
                pass;
            elif step=='4':
                name = reginfo.get('username','');
                if name!='':
                    if _username_check(name):
                        return HttpResponse(NOERROR,content_type="application/json")
                    else:
                        return HttpResponse(REGISTER_USER_EXIST,content_type="application/json")
            elif step=='5':
                pass;
            elif step=='6':
                if create_user(reginfo):
                    set_userprofile(reginfo);
                    return HttpResponse(REGISTER_SUCCESS ,content_type="application/json")
                else:
                    return HttpResponse(REGISTER_USER_EXIST ,content_type="application/json")
            else:
                return HttpResponse(INVALIDE_JSON,content_type="application/json")
                
        else:
            return HttpResponse(INVALIDE_JSON,content_type="application/json")
  
    return HttpResponse(INVALIDE_JSON,content_type="application/json")