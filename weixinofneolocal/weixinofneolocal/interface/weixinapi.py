# -*- coding: utf-8 -*-
"""
Created on Thu Nov  6 11:08:09 2014

@author: root
"""

# coding=utf-8
import urllib
import urllib2
import hashlib
import json
import time
import random
from lxml import etree
from django.utils.encoding import smart_str
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from interface.utils import *
from config.config import *
from app.menu import *
from xml_api import *
from interface.servctrl import *

@csrf_exempt
# commonutil = WeixinUtil()
class WeixinInterface:
    def __init__(self, token, appid, secret):
        self.token = token
        self.appid = appid
        self.secret = secret
        self.commonutil = WeixinUtil()
        self.sctrl = BasicCtrl()
        self.a_token = Access_Token()
        self.au_token = Auth_Token()
        # self.createMenu(self.get_access_token(), my_menu)
	
    def checkSignature(self, request):
        signature = request.GET.get("signature", None)
        timestamp = request.GET.get("timestamp", None)
        nonce = request.GET.get("nonce", None)
        echostr = request.GET.get("echostr", None)
        tmp_list = [self.token, timestamp, nonce]
        tmp_list.sort()
        tmp_str = "%s%s%s" % tuple(tmp_list)
        tmp_str = hashlib.sha1(tmp_str).hexdigest()
        if tmp_str == signature:
            return echostr
        else:
            return "Auth not passed"
        
    def get_access_token(self):
        cur_time = int(time.time())
        tmp = cur_time - self.a_token.ACCESS_TOKEN_TIME
        if tmp < self.a_token.expires_in:
            access_token = self.a_token.ACCESS_TOKEN
            return access_token
        
        url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s' % (self.appid, self.secret)
        data = self.commonutil.method_get_api(url)
        access_token = data.get("access_token")
        self.a_token.ACCESS_TOKEN_TIME = cur_time
        self.a_token.ACCESS_TOKEN = access_token
        return access_token
    
    
    def isCodeRequest(self, request):
        code = request.GET.get('code', None);
        if code != None:
            return True;
        return False;
             
    def getUserCode(self, request):
        code = request.GET.get('code', None);
        state = request.GET.get('state', None);
      
        if code == None:
            if state != None:
            	return None;
             
        return code;
    
    def isLocalAuthTokenEmpty(self):
        if self.au_token.TOKEN:
            return False
        return True
        
    def isAuthTokenValide(self):
        if self.isLocalAuthTokenEmpty():
            return None;
        
        url = 'https://api.weixin.qq.com/sns/auth?access_token=%s&openid=%s' % (self.au_token.TOKEN, self.au_token.OPENID)
        data = self.commonutil.method_get_api(url)
        errcode = data.get("errcode")
        if errcode:
            errmsg = data.get("errmsg")
            print '%s' , errmsg
            return False
        return True
        
    def refreshAuthToken(self):
        if self.au_token.REFTOKEN == None:
            return None;
        url = 'https://api.weixin.qq.com/sns/oauth2/refresh_token?appid=%s&grant_type=refresh_token&refresh_token=%s' % (self.appid, au_token.REFTOKEN);
        data = self.commonutil.method_get_api(url);
        
        if len(data) == 2:
            errcode = data.get("errcode");
            errmsg = data.get("errmsg");
            print '%s' , errmsg;
            return errcode;
        
        self.au_token.TOKEN = data.get("access_token");
        self.au_token.OPENID = data.get("openid");
        self.au_token.REFTOKEN = data.get("refresh_token");
        self.au_token.SCOPE = data.get("scope");
        
        return self.au_token;
        
    def getAuthToken(self, request=None):
        code = self.getUserCode(request);

        url = 'https://api.weixin.qq.com/sns/oauth2/access_token?appid=%s&secret=%s&code=%s&grant_type=authorization_code' % (self.appid, self.secret, code);
        data = self.commonutil.method_get_api(url);
        
        if len(data) == 2:
            errcode = data.get("errcode");
            errmsg = data.get("errmsg");
            print '%s' , errmsg;
            return errcode;
        
        self.au_token.TOKEN = data.get("access_token");
        self.au_token.OPENID = data.get("openid");
        self.au_token.REFTOKEN = data.get("refresh_token");
        self.au_token.SCOPE = data.get("scope");
        # return self.au_token;
        return self.au_token;
             
   
    def getAuthUserInfo(self, request):
        if self.isAuthTokenValide() != True:
            auth_token = self.getAuthToken(request);
        else:
            auth_token = self.refreshAuthToken();
            
        url = 'https://api.weixin.qq.com/sns/userinfo?access_token=%s&openid=%s&lang=zh_CN' % (auth_token.TOKEN, auth_token.OPENID);
        data = self.commonutil.method_get_api(url);
        
        if len(data) == 2:
            errcode = data.get("errcode");
            errmsg = data.get("errmsg");
            print '%s' , errmsg;
            return errcode;
        # write to db
        open_id = data.get("openid");
        if self.sctrl.isUserExist(open_id):
            return open_id;
        
        gid = self.getGroupidOfUser(open_id);
        """
        data.get("privilege")
        """
        return self.sctrl.setUserInfo(data, gid);
    
    def doUserAuth(self, appid=urllib.quote(WEIXIN_APPID), rurl=urllib.quote(REDIRECT_URL)):
        url = 'https://open.weixin.qq.com/connect/oauth2/authorize?appid=%s&redirect_uri=%s&response_type=code&scope=snsapi_userinfo&state=123#wechat_redirect' % (appid, rurl)
        # data = method_get_api(url)
        return HttpResponseRedirect(url)

    def get_user_openid(self, appid, secret, code):
        url = 'https://api.weixin.qq.com/sns/oauth2/access_token?appid=%s&\
        secret=%s&code=%s&grant_type=authorization_code' % (self.appid, self.secret, code)
        data = self.commonutil.method_get_api(url)
        openid = data.get("openid")
        return openid
    
    def createMenu(self, post_data=app_menu4):
        access_token = self.get_access_token()
        
        url = 'https://api.weixin.qq.com/cgi-bin/menu/create?access_token=%s' % (access_token)
        data = self.commonutil.method_post_api(url, post_data)
        errcode = data.get("errcode")
        if errcode != 0:
            errmsg = data.get("errmsg")
            print '%s' , errmsg
        return errcode
    
    def deleteMenu(self):
        access_token = self.get_access_token()
        
        url = 'https://api.weixin.qq.com/cgi-bin/menu/delete?access_token=%s' % (access_token)
        data = self.commonutil.method_get_api(url)
        errcode = data.get("errcode")
        return errcode
    
    def createGroup(self, g_name):
        access_token = self.get_access_token()
        
        url = 'https://api.weixin.qq.com/cgi-bin/groups/create?access_token=%s' % (access_token)
        group = {"group":{"name":g_name}}
        data = self.commonutil.method_post_api(url, json.dumps(group))
        
        if len(data) == 2:
            errcode = data.get("errcode")
            errmsg = data.get("errmsg")
            print '%s' , errmsg
            return errcode
        return 0
            
    def getAllGroupInfo(self):
        access_token = self.get_access_token()
        
        url = 'https://api.weixin.qq.com/cgi-bin/groups/get?access_token=%s' % (access_token)
        data = self.commonutil.method_get_api(url)
        
        if len(data) == 2:
            return None
        list = data.get("groups")
        list_len = len(list)
        for i in range(0, list_len):
            gid = list[i].get("id")
            if not self.sctrl.isGroupExist(gid):
                name = list[i].get("name")
                count = list[i].get("count")
                self.sctrl.setGroupInfo(gid, name, count)
        return list
            
    def getGroupidOfUser(self, openid):
        access_token = self.get_access_token()
        
        url = 'https://api.weixin.qq.com/cgi-bin/groups/getid?access_token=%s' % (access_token)
        post_data = {"openid":openid}
        data = self.commonutil.method_post_api(url, post_data)
        
        if len(data) == 2:
            errcode = data.get("errcode")
            errmsg = data.get("errmsg")
            print '%s' , errmsg
            return errcode
        gid = data.get("groupid")
        return gid
    
    def changeGroupName(self, id, gname):
        access_token = self.get_access_token()
        url = 'https://api.weixin.qq.com/cgi-bin/groups/update?access_token=%s' % (access_token)
        post_data = {"group":{"id":id, "name":gname}}
        data = self.commonutil.method_postjson_api(url, post_data)
        # write to db
        errcode = data.get("errcode")
        if errcode != 0:
            errmsg = data.get("errmsg")
            print '%s' , errmsg
            return errcode
        return errcode
    
    def getUserInfo(self, openid):
        access_token = self.get_access_token()
        
        if self.sctrl.isUserExist(openid):
            return 0
            
        gid = self.getGroupidOfUser(openid)
        url = 'https://api.weixin.qq.com/cgi-bin/user/info?access_token=%s&openid=%s&lang=zh_CN' % (access_token, openid)
        data = self.commonutil.method_get_api(url)
        
        if len(data) == 2:
            errcode = data.get("errcode")
            errmsg = data.get("errmsg")
            print '%s' , errmsg
            return errcode
            
        return self.sctrl.setUserInfo(data, gid)
        
    def getFucosUsersInfo(self):
        """当用户超过10000时需要改动
        """
        access_token = self.get_access_token()
        
        url = 'https://api.weixin.qq.com/cgi-bin/user/get?access_token=%s&next_openid=' % (access_token)
        data = self.commonutil.method_get_api(url)
        
        if len(data) == 2:
            errcode = data.get("errcode")
            errmsg = data.get("errmsg")
            print '%s' , errmsg
            return errcode
            
        num = data.get("count")
        list = data.get("data").get("openid")
        for i in range(0, num):
            self.getUserInfo(list[i])
        
        return data
    
    def sendXmlMsg(self, xml):
        pass
    
    def sendJsonMsg(self, post_data):
        access_token = self.get_access_token();
        url = "https://api.weixin.qq.com/cgi-bin/message/custom/send?access_token=%s" % (access_token);
        return self.commonutil.method_postjson_api(url, post_data);
    
    def msgNotifyApi(self, touserid, msgtype='text'):
        if msgtype == 'text':
            data = self.sctrl.getRspText("tinfo");
            return self.sendJsonMsg(text_reply_json(touserid, data));
        elif msgtype == 'image':
            data = self.sctrl.getRspImage("picinfo");
            return self.sendJsonMsg(image_reply_json(touserid, data));
        elif msgtype == 'voice':
            data = self.sctrl.getRspVoice("voinfo");
            return self.sendJsonMsg(voice_reply_json(touserid, data));
        elif msgtype == 'music':
            data = self.sctrl.getRspMusic("minfo");
            return self.sendJsonMsg(music_reply_json(touserid, data));
        elif msgtype == 'video':
            data = self.sctrl.getRspVideo("vinfo");
            return self.sendJsonMsg(media_reply_json(touserid, data));
        elif msgtype == 'news':
            data = self.sctrl.getRspNews("ninfo");
            return self.sendJsonMsg(news_reply_json(touserid, data));
        else:
            pass;
            
    def msgNotifyXmlApi(self, touserid, msgtype='text'):
        if msgtype == 'text':
            data = self.sctrl.getRspText("tinfo");
            return text_reply_xml(touserid, data);
        elif msgtype == 'subscribe':
            data = self.sctrl.getRspText("subscribe");
            return text_reply_xml(touserid, data);
        elif msgtype == 'image':
            data = self.sctrl.getRspImage("picinfo");
            return image_reply_xml(touserid, data);
        elif msgtype == 'voice':
            data = self.sctrl.getRspVoice("voinfo");
            return voice_reply_xml(touserid, data);
        elif msgtype == 'music':
            data = self.sctrl.getRspMusic("minfo");
            return music_reply_xml(touserid, data);
        elif msgtype == 'video':
            data = self.sctrl.getRspVideo("vinfo");
            return media_reply_xml(touserid, data);
        elif msgtype == 'news':
            data = self.sctrl.getRspNews("ninfo");
            return news_reply_xml(touserid, data);
        else:
            pass;
    
    def notifyToAll(self, msgtype='text'):
        userlist = self.sctrl.getAllUserInfo();
        for i in range(0, len(userlist)):
        	self.msgNotifyApi(userlist[i].userid, msgtype);
        return;
            
    
    def testMsgApi(self, text):
        data = text_reply_json("okOD_suoJyb158onn-fox9HojiGc", text);
        return self.sendJsonMsg(data);
    
    def dealLocationMsg(self, xml_req):
        return self.sctrl.setLocationInfo(xml_req);
        
    def reccordMsg(self, xml_req):
        self.sctrl.setMsgRecord(xml_req);
        return "i am fucking ended"
    
    def uploadFile(self, ftype, fullname):
        ''' {"type":"TYPE","media_id":"MEDIA_ID","created_at":123456789}
        媒体文件类型，分别有图片（image）、语音（voice）、视频（video）和缩略图（thumb，主要用于视频与音乐格式的缩略图） '''
        access_token = self.get_access_token();
        url = 'http://file.api.weixin.qq.com/cgi-bin/media/upload?access_token=%s&type=%s' % (access_token, ftype);
        if ftype == 'image':
            contype = 'image/' + self.commonutil.method_get_namelist(fullname)[1];
        elif ftype == 'voice':
            contype = 'application/x-jpg';
        elif ftype == 'video':
            contype = 'application/x-jpg';
        elif ftype == 'thumb':
            contype = 'application/x-jpg';
        else:
            return None;
            
        resp = self.commonutil.method_http_upload(url, fullname, contype);
        data = json.loads(resp);
        if len(data) == 2:
            errcode = data.get("errcode")
            errmsg = data.get("errmsg")
            print '%s' , errmsg
            return errcode
        
        # self.sctrl.setFileInfo(data);
        
        return resp;
    
    def downloadFile(self, mediaid, filename):
        '''HTTP/1.1 200 OK
        Connection: close
        Content-Type: image/jpeg 
        Content-disposition: attachment; filename="MEDIA_ID.jpg"
        Date: Sun, 06 Jan 2013 10:20:18 GMT
        Cache-Control: no-cache, must-revalidate
        Content-Length: 339721'''
        import base64
        access_token = self.get_access_token();
        url = 'http://file.api.weixin.qq.com/cgi-bin/media/get?access_token=%s&media_id=%s' % (access_token, mediaid);
        resp = self.commonutil.method_http_download(url, filename);
        self.sctrl.setMediaMsg(mediaid, base64.b64encode(resp));
        return resp;
    # life = 1800
    def createTmpScanCode(self, sceneid):
        access_token = self.get_access_token();
        url = 'https://api.weixin.qq.com/cgi-bin/qrcode/create?access_token=%s' % access_token;
        jsondata = {"expire_seconds": 1800, "action_name": "QR_SCENE", "action_info": {"scene": {"scene_id": sceneid}}}
        data = self.commonutil.method_post_api(url, jsondata);
        if len(data) == 2:
            errcode = data.get("errcode");
            errmsg = data.get("errmsg");
            print '%s' , errmsg;
            return errcode;
        return data.get('ticket');
    
    def createScanCode(self, sceneid):
        access_token = self.get_access_token();
        url = 'https://api.weixin.qq.com/cgi-bin/qrcode/create?access_token=%s' % access_token;
        jsondata = {"action_name": "QR_LIMIT_SCENE", "action_info": {"scene": {"scene_id": sceneid}}}
        data = self.commonutil.method_post_api(url, jsondata);
        if len(data) == 2:
            errcode = data.get("errcode");
            errmsg = data.get("errmsg");
            print '%s' , errmsg;
            return errcode;
        # return data.get('ticket');
        return data;
        
    def getScanCodePic(self, ticket):
        # url = 'https://mp.weixin.qq.com/cgi-bin/showqrcode?ticket=%s' % urllib2.quote(ticket);
        url = 'https://mp.weixin.qq.com/cgi-bin/showqrcode?ticket=%s' % ticket;
        data = self.commonutil.method_http_download(url);
        return data;
        
            

        
    
    
        
    
     
    
    
        
    
    
