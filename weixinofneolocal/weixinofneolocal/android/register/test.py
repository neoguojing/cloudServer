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

    
def register_test(request):
    data = util.method_postjson_api("http://101.88.10.85:10000/site1/android/register/",
                                    register_json);
    return HttpResponse(json.dumps(data),content_type="application/json")
    