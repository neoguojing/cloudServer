# coding=utf-8
import urllib2
import json
import os
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from utils.sae_storage import *

@csrf_exempt
class NeoUeditor:
    def __init__():
        pass;
    
    def __method_get_api(self, url):
        response = urllib2.urlopen(url).read()
        dict_data = json.loads(response)
        return dict_data
    
    def __method_post_api(self, url, post_data):
        if post_data:
            json_data = json.dumps(post_data, ensure_ascii=False).encode('utf8')
        else:
            return ''
        print 'json_data==', json_data
        req = urllib2.Request(url, json_data)
        req.add_header('Context-Type', 'application/json;charset=utf-8')
        return_json = urllib2.urlopen(req).read()
        return json.loads(return_json)
    
    def __method_get_namelist(self, fullname):
        filename = self.__method_get_filename(fullname);
        return filename.split('.');
    
    def __method_get_filename(self, fullname):
        filename = os.path.basename(fullname);
        return filename;
    
    def __saveUploadData(self, filepath, data, filetype, callback=setToSAEStorage):
        filename = self.__method_get_filename(filepath);
        return callback(filename, data, filetype);
    
    def __geneResponse(self):
        feedback = u'''{
            "state": %s,
            "url": %s,
            "title": %s,
            "original": %s
        }''' % ()
        return feedback;
    
    def doFileUpload(self, request):
        fileObj = request.FILES.get('upfile', None);
        title = request.POST.get('pictitle', '');
        filename = request.POST.get('fileName', '');
        self.__saveUploadData(filename, fileObj, filetype);
        return;
        
    
    
