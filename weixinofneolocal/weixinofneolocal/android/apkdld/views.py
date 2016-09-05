#coding=utf-8
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from config.settings import ROOT_PATH
from ..models import *
from utils.download import *

    
def apk_download(request,name,version):
    
    filepath = "";
    myapk = MyApk.objects.filter(name=name).filter(version=version).latest('creaion_time');
    filepath = ROOT_PATH+myapk.apk.url;

    return fast_download(request,filepath);
    
def apk_list(request):
    
    apklist = MyApk.objects.all();

    return render_to_response('apkdld/apklist.html',
                              {'apklist':apklist},
        context_instance=RequestContext(request));