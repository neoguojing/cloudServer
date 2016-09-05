# -*- coding: utf-8 -*-
#coding=utf-8
from django.http import StreamingHttpResponse
from django.http import HttpResponse
from django.utils.encoding import smart_str
from django.core.servers.basehttp import FileWrapper  
import os, tempfile, zipfile  

media_path = '/home/neo/workspace/weixinofneolocal/weixinofneolocal/media/';

def big_file_download(request,the_file_name):
    # do something...    
    def file_iterator(file_name, chunk_size=512):
        with open(file_name) as f:
            while True:
                c = f.read(chunk_size)
                if c:
                    yield c
                else:
                    break

    response = StreamingHttpResponse(file_iterator(the_file_name))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Length'] = os.path.getsize(the_file_name)
    response['Content-Disposition'] = 'attachment;filename=%s' % the_file_name.split("/")[-1]

    return response

def big_file_download1(request,filepath):
    wrapper = FileWrapper(file(filepath))
    response = HttpResponse(wrapper, content_type='application/octet-stream')
    response['Content-Length'] = os.path.getsize(filepath)
    response['Content-Disposition'] = 'attachment; filename=%s' % filepath.split("/")[-1]
    return response

def zip_file_download(request,zipfilename,*filestozip):
    # do something...
    temp = tempfile.TemporaryFile()  
    archive = zipfile.ZipFile(temp, 'w', zipfile.ZIP_DEFLATED)  
    for doc in filestozip:  
        filepath = doc # Select your files here.                             
        archive.write(filepath, '%' % filepath.split("/")[-1])  
    archive.close()  
    wrapper = FileWrapper(temp)  

    response = HttpResponse(wrapper, content_type='application/zip')
    response['Content-Disposition'] = 'attachment;filename=%s' % (zipfilename)
    response['Content-Length'] = temp.tell()  
    temp.seek(0)  
    return response


def fast_download(request,filepath):
    response = HttpResponse(content_type='application/octet-stream') 
    response['Content-Disposition'] = 'attachment; filename=%s' % smart_str(filepath.split("/")[-1])
    response['Content-Length'] = os.path.getsize(filepath)
    response['X-Sendfile'] = smart_str(filepath)
    
    return response
    
def force_download(request,filepath):
    response = HttpResponse(content_type='application/force-download') 
    response['Content-Disposition'] = 'attachment; filename=%s' % smart_str(filepath.split("/")[-1])
    response['Content-Length'] = os.path.getsize(filepath)
    response['X-Sendfile'] = smart_str(filepath)
    
    return response
    
def image_download(request,filepath,name):
    response = HttpResponse(content_type='application/octet-stream') 
    suffix = filepath.split(".")[-1]
    response['Content-Disposition'] = 'attachment; filename=%s' % smart_str(name)
    response['Content-Length'] = os.path.getsize(filepath)
    response['X-Sendfile'] = smart_str(filepath)
    
    return response