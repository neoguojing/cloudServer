# coding=utf-8
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from utils.ueditor13.config import *
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from utils.sae_storage import *
from utils.ueditor13.ueditor import *
# import Image
import os
import time
import urllib2
import uuid

def main(request):
    
    if request.GET.get('fetch', None) != None:
        return HttpResponse(getImagePathConfig(), content_type="application/json"); 
    
    action = request.GET.get('action', None);
    result = '';
    if action == 'config':
        result = getUeditorConfig1();
        # ue = NeoUeditor(request);
        # result = ue.saveUploadData("test.txt","hello world fuck");
        # return HttpResponseRedirect('http://weixinofneo.sinaapp.com/err/');
    elif action == 'uploadimage':
        return HttpResponse(request.REQUEST);
    elif action == 'uploadscrawl':
        setToSAEStorage('cralupload.txt', request.REQUEST, 'txt');
        return HttpResponse(request.REQUEST);
    elif action == 'uploadvideo':
        return HttpResponse(request.REQUEST);
    elif action == 'uploadfile':
        setToSAEStorage('fileupload.txt', request.REQUEST, 'txt');
        return HttpResponse(request.REQUEST);
    elif action == 'listimage':
        return HttpResponse(request.REQUEST);
    elif action == 'catchimage':
        return HttpResponse(request.REQUEST);
    else:
        ue = NeoUeditor(request);
        result = ue.doFileUpload();
    
    cb = request.GET.get('callback', None)
    if  cb != None:
        result = cb + '(' + result + ')';
    
    return HttpResponse(result, content_type="application/json"); 
	# return HttpResponse(result);
    
def imageUp(request):
    response = HttpResponse();
    if request.GET.get('fetch', None) != None:
        result = getImagePathConfig();
    	response.write(result);
        return response;
    ue = NeoUeditor(request);
    return HttpResponse(ue.doFileUpload(), content_type="application/json");
    # return HttpResponse(ue.geneResponse(),content_type="application/json");

def fileUp(request):
    # ue = NeoUeditor(request);
    # result = ue.saveUploadData("test.txt","hello world fuck");
    # return HttpResponse(ue.geneResponse(),content_type="application/json");
    if request.GET.get('fetch', None) != None:
        return HttpResponse(getImagePathConfig(), content_type="application/json"); 
    ue = NeoUeditor(request);
    return HttpResponse(ue.doFileUpload(), content_type="application/json");

def scrawUp(request):
    ue = NeoUeditor(request);
    return HttpResponse(ue.doScrowUp());


def fileMgnt(request):
    ue = NeoUeditor(request);
    return HttpResponse(ue.imageManager());

def videoUp(request):
    ue = NeoUeditor(request);
    return HttpResponse(ue.doFileUpload());

def wordUp(request):
    ue = NeoUeditor(request);
    return HttpResponse(ue.doFileUpload());

def screenUp(request):
    ue = NeoUeditor(request);
    return HttpResponse(ue.doFileUpload());

def catchUp(request):
    ue = NeoUeditor(request);
    return HttpResponse(ue.getRemoteImage());


def videoOnlion(request):
    ue = NeoUeditor(request);
    return HttpResponse(ue.getMovie());

def LoadUeditor(request):
    return render_to_response('index13.html');
