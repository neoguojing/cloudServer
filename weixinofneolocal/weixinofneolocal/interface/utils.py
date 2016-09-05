# coding:utf8
import datetime
import hashlib
import os
import urllib
import urllib2
import json
import logging
import time

from django.conf import settings
from django.core.cache import cache
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

'''
#buld post body data
        boundary = '----------%s' % hex(int(time.time() * 1000))
        data = []
        data.append('--%s' % boundary)
        
        data.append('Content-Disposition: form-data; name="%s"\r\n' % 'username')
        data.append('jack')
        data.append('--%s' % boundary)
        
        data.append('Content-Disposition: form-data; name="%s"\r\n' % 'mobile')
        data.append('13800138000')
        data.append('--%s' % boundary)
        
        fr=open(r'/var/qr/b.png','rb')
        data.append('Content-Disposition: form-data; name="%s"; filename="b.png"' % 'profile')
        data.append('Content-Type: %s\r\n' % 'image/png')
        data.append(fr.read())
        fr.close()
        data.append('--%s--\r\n' % boundary)
    
        http_url='http://remotserver.com/page.php'
        http_body='\r\n'.join(data)
        try:
            #buld http request
            req=urllib2.Request(http_url, data=http_body)
            #header
            req.add_header('Content-Type', 'multipart/form-data; boundary=%s' % boundary)
            req.add_header('User-Agent','Mozilla/5.0')
            req.add_header('Referer','http://remotserver.com/')
            #post data to server
            resp = urllib2.urlopen(req, timeout=5)
            #get response
            qrcont=resp.read()
            print qrcont
            
            
        except Exception,e:
            print 'http error'
            
        #下载
         resp = urllib2.urlopen(req, timeout=5)
         qrcont=resp.read();
         with open("filename","wb") as code;
         code.write(qrcont);
         def downloadfile(file_url,filename,download_path):
    try:
        request = urllib2.Request(file_url) 
        f=open(download_path+filename,'wb')
        start_time=time.time()
        #print 'time stamp is : ',time.time()
        print start_time 
        size =0
        speed=0
        data_lines = urllib2.urlopen(request).readlines()
        #data = urllib2.urlopen(request).read() 
        for data in data_lines:
            f.write(data)
            size = size + len(data)
            dural_time=float(time.time()) - float(start_time)
            if(dural_time>0):
                speed = float(size)/float(dural_time)/(1000*1000)
                while(speed >1):
                    print 'speed lagger than 1MB/s , sleep(0.1).....'
                    print 'sleep .....'
                    sleep(0.1)
                    dural_time=float(time.time()) - float(start_time)
                    speed = float(size)/float(dural_time)/(1000*1000)
        print 'total time is : ',dural_time ,'seconds'
        print 'size is       : ',size ,'KB'
        print 'speed is      : ',speed ,'MB/s'  
    except Exception,e:
        print 'download error: ',e
        return False
    return True
'''

class WeixinUtil:
    def method_get_api(self, url):
        response = urllib2.urlopen(url).read()
        dict_data = json.loads(response)
        return dict_data
    
    def method_post_api(self, url, post_data):
        if post_data:
            json_data = json.dumps(post_data, ensure_ascii=False).encode('utf8')
        else:
            return ''
        print 'json_data==', json_data
        req = urllib2.Request(url, json_data)
        req.add_header('Context-Type', 'application/json;charset=utf-8')
        return_json = urllib2.urlopen(req).read()
        return json.loads(return_json)
    
    def method_postjson_api(self, url, post_data):
        req = urllib2.Request(url, post_data)
        req.add_header('Context-Type', 'application/json;charset=utf-8')
        return_json = urllib2.urlopen(req).read()
        return json.loads(return_json)
        
    def method_get_log(self, app_name):
        log = logging.getLogger(app_name)
        log.setLevel(__debug__)
        return log
    
    def method_get_namelist(self, fullname):
        filename = os.path.basename(fullname);
        return filename.split('.');
    
    def method_http_upload(self, url, fullname, contype):
        boundary = '----------%s' % hex(int(time.time() * 1000));
        filename = os.path.basename(fullname);
        contid = filename.split('.')[0];
        
        data = [];
        data.append('--%s' % boundary);
        
        fr = open(fullname, 'rb');
        data.append('Content-Disposition: form-data; name="%s"; filename="%s"' % (contid, filename));
        data.append('Content-Type: %s\r\n' % contype);
        data.append(fr.read());
        fr.close();
        data.append('--%s--\r\n' % boundary);
        
        # http_url='http://remotserver.com/page.php'
        http_body = '\r\n'.join(data);
        try:
            # buld http request
            req = urllib2.Request(url, data=http_body);
            # header
            req.add_header('Content-Type', 'multipart/form-data; boundary=%s' % boundary);
            req.add_header('User-Agent', 'Mozilla/5.0');
            # req.add_header('Referer','http://weixinofneo.sinapp.com');
            req.add_header('Referer', settings.DOMAIN_NAME)
            # post data to server
            resp = urllib2.urlopen(req, timeout=5);
            # get response
            qrcont = resp.read();
            print qrcont;
            return qrcont;
            
        except Exception, e:
            print 'http error';
            return e
    
    def method_httptext_download(self, file_url, filename, download_path):
        try:
            request = urllib2.Request(file_url) 
            f = open(download_path + filename, 'wb')
            start_time = time.time()
            # print 'time stamp is : ',time.time()
            print start_time 
            size = 0
            speed = 0
            data_lines = urllib2.urlopen(request).readlines()
            # data = urllib2.urlopen(request).read() 
            for data in data_lines:
                f.write(data)
                size = size + len(data)
                dural_time = float(time.time()) - float(start_time)
                if(dural_time > 0):
                    speed = float(size) / float(dural_time) / (1000 * 1000)
                    while(speed > 1):
                        print 'speed lagger than 1MB/s , sleep(0.1).....'
                        print 'sleep .....'
                        time.sleep(0.1)
                        dural_time = float(time.time()) - float(start_time)
                        speed = float(size) / float(dural_time) / (1000 * 1000)
            print 'total time is : ', dural_time , 'seconds'
            print 'size is       : ', size , 'KB'
            print 'speed is      : ', speed , 'MB/s'  
        except Exception, e:
            print 'download error: ', e
            return False
        return True
        
    def method_http_download(self, url, fullname=None):
        '''HTTP/1.1 200 OK
        Connection: close
        Content-Type: image/jpeg 
        Content-disposition: attachment; filename="MEDIA_ID.jpg"
        Date: Sun, 06 Jan 2013 10:20:18 GMT
        Cache-Control: no-cache, must-revalidate
        Content-Length: 339721
        curl -G "http://file.api.weixin.qq.com/cgi-bin/media/get?access_token=ACCESS_TOKEN&media_id=MEDIA_ID"'''
        try:
           # f=open(fullname,'wb');
            data = urllib2.urlopen(url).read();
           # f.write(data);
        
        except Exception, e:
            print 'download error: ', e;
            return e;
        return data
