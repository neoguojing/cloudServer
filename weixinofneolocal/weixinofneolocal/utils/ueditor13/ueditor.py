# coding=utf-8
import urllib2
import json
import os
import uuid
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import base64

from django.conf import settings
if settings.ENV == 'SAE':
    from utils.sae_storage import *
    saveUploadFile = setToSAEStorage
elif settings.ENV == 'VM':
    from utils.storage.base import *
    storage = NeoStorage(settings.MEDIA_ROOT)
    saveUploadFile = storage.saveUploadFile
    
    

@csrf_exempt
class NeoUeditor:
    __filename = '';
    __state = 'SUCCESS';
    __url = '';
    __title = '';
    __request = None;
    __fileobj = None;
    __prefix = '';
    
    def __init__(self, request, prefixofpath='http://weixinofneo-media.stor.sinaapp.com/'):
        self.__request = request;
        self.__prefix = prefixofpath;
        # self.doFileUpload();
        
    def __method_http_download(self, url):
        try:
            data = '';
            data = urllib2.urlopen(url).read();
        except Exception, e:
            print 'download error: ', e;
        return data;
        
    
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
        if fullname != '':
            filename = self.__method_get_filename(fullname);
            m_list = filename.split('.');
            if len(m_list) <= 1:
                return None;
            return m_list;
    	return None
    
    def __method_get_filename(self, fullname):
        filename = os.path.basename(fullname);
        return filename;
    
    def __saveUploadData(self, filename, data, callback=saveUploadFile):
        if data == None:
            return self.__geneResponse("No File!");
        
        save_name = str(uuid.uuid1()) + '_' + filename;
        self.__url = callback(save_name, data);
        if self.__url == None:
            return self.__geneResponse("FAILED")
        return self.__geneResponse();
    
    def __geneResponse(self, statu='SUCCESS'):
        self.__state = statu
        feedback = '''{"original": %s,"url": %s,"title": %s,"state": %s}''' % (self.__filename, self.__url, self.__title, self.__state);
        return feedback;
    
    def doFileUpload(self):
        self.__fileObj = self.__request.FILES.get('upfile', None);
        self.__title = self.__request.POST.get('pictitle', '');
        self.__filename = self.__request.POST.get('fileName', '');
        if self.__filename == '':
            self.__filename = self.__request.POST.get('filename', '');
        return self.__saveUploadData(self.__filename, self.__fileobj);
        # return self.saveUploadData();
    
    def doScrowUp(self):
        """ 涂鸦文件,处理 """
        param = self.__request.POST.get("action", '');
    
        if  param == 'tmpImg':
            resp = self.doFileUpload();
            resp = dict(resp);
            return "<script>parent.ue_callback('%s','%s')</script>" % (resp.get('url', ''), resp.get('state', ''));
            
        else:
            #========================base64上传的文件=======================
            self.__fileObj = self.__request.POST.get('content', '');
            self.__filename = str(uuid.uuid1()) + '.png';
            resp = self.__saveUploadData(self.__filename, base64.decodestring(str(self.__fileobj)));
            resp = dict(resp);
            return "{'url':'%s',state:'%s'}" % (resp.get('url', ''), resp.get('state', ''));
    
    def __listDir(self, path, filelist):
        """ 递归 得到所有图片文件信息 """
        phisypath = settings.MEDIA_ROOT[0] if isinstance(settings.MEDIA_ROOT , list) else settings.MEDIA_ROOT
        if os.path.isfile(path):
            return '[]'
        allFiles = os.listdir(path)
        retlist = []
        for cfile in allFiles:
            fileinfo = {}
            filepath = (path + os.path.sep + cfile).replace("\\", "/").replace('//', '/')
    
            if os.path.isdir(filepath):
                self.__listDir(filepath, filelist)
            else:
                if cfile.endswith('.gif') or cfile.endswith('.png') or cfile.endswith('.jpg') or cfile.endswith('.bmp'):
                    filelist.append(filepath.replace(phisypath, '/upload/').replace("//", "/"))
    
    if settings.ENV == 'SAE':
        def __listDirSAE(self, path='', callback=listDirOfSAEStorage):
            saelist = callback(path);
            filelist = [];
            for i in range(0, len(saelist)):
                filelist.append(self.__prefix + saelist[i].get('name'));
            return filelist;
    
    @csrf_exempt
    def imageManager(self):
        """ 图片在线管理  """
        path = '';
        filelist = self.__listDirSAE(path);
        
        imgStr = "ue_separate_ue".join(filelist);
        response = HttpResponse();
        response.write(imgStr);
        return response;
    
    
    @csrf_exempt
    def getMovie(self):
        """ 获取视频数据的地址 """
        content = ""
        searchkey = self.__request.POST.get("searchKey")
        videotype = self.__request.POST.get("videoType")
        try:
            url = "http://api.tudou.com/v3/gw?method=item.search&appKey=myKey&format=json&kw=" + searchkey + "&pageNo=1&pageSize=20&channelId=" + videotype + "&inDays=7&media=v&sort=s"
            content = urllib2.urlopen(url).read()
        except Exception, e:
            print e;
            return e;
        response = HttpResponse()
        response.write(content)
        return response
    
    
    @csrf_exempt
    def getRemoteImage(self):
        """ 把远程的图抓到本地,爬图 """
        #====get request params=================================
        urls = str(self.__request.POST.get("upfile", ''))
        urllist = urls.split("ue_separate_ue")
        outlist = []
        #====request params end=================================
        for self.__url in urllist:
            # 获取文件ming
            self.__filename = self.__method_get_filename(self.__url);
            # 下载并保存图片
            self.__fileObj = self.__method_http_download(self.__url);
            rsp = self.__saveUploadData(self.__filename, self.__fileObj);
            rsp = dict(rsp);
            outlist.append(rsp.get('url'));
        outlist = "ue_separate_ue".join(outlist)
        # 需要加入错误码处理
        response = HttpResponse()
        myresponse = "{'url':'%s','tip':'%s','srcUrl':'%s'}" % (outlist, u'成功', urls)
        response.write(myresponse)
        return response
        
    def geneResponse(self, statu='SUCCESS'):
        self.__state = statu
        feedback = {"url": self.__url, "title": self.__title, "original": self.__filename, "state": self.__state, };
        return feedback;
    
    def saveUploadData(self, filename="test.sh", data="quni mabi", callback=saveUploadFile):
        if data == None:
            return self.__geneResponse("No File!");
        
        save_name = str(uuid.uuid1()) + '_' + filename;
        self.__url = callback(save_name, data);
        if self.__url == None:
            return self.__geneResponse("FAILED")
        return self.__geneResponse();
        
    
    
