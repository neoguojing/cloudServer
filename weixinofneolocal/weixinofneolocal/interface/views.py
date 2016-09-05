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
from interface.utils import *
from lxml import etree
from config.config import *
from menu import *
from xml_api import *
from django.utils.encoding import smart_str
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

@csrf_exempt
# commonutil = WeixinUtil()
class WeixinInterface:
    def __init__(self, token, appid, secret):
        self.token = token
        self.appid = appid
        self.secret = secret
        self.commonutil = WeixinUtil()
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
            return None
            
    def get_access_token(self):
        cur_time = int(time.time())
        tmp = cur_time - Access_Token.ACCESS_TOKEN_TIME
        if tmp < Access_Token.expires_in:
            access_token = Access_Token.ACCESS_TOKEN
            return access_token
        url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_\
        credential&appid=%s&secret=%s' % (self.appid, self.secret)
        data = self.commonutil.method_get_api(url)
        access_token = data.get("access_token")
        Access_Token.ACCESS_TOKEN_TIME = cur_time
        Access_Token.ACCESS_TOKEN = access_token
        return access_token

    def get_user_openid(self, appid, secret, code):
        url = 'https://api.weixin.qq.com/sns/oauth2/access_token?appid=%s&\
        secret=%s&code=%s&grant_type=authorization_code' % (self.appid, self.secret, code)
        data = method_get_api(url)
        openid = data.get("openid")
        return openid
        
    def auto_reply(self, request_xml):
        """识别消息的类型 分类处理
        """
        msg_type = request_xml.find("MsgType").text
        from_user_name = request_xml.find("FromUserName").text
        if msg_type == "text":
            content = request_xml.find("Content").text
            return HttpResponse(self.find_reply(from_user_name, content))
        elif msg_type == "text":
            pass
        elif msg_type == "image":
            pass
        elif msg_type == "voice":
            pass
        elif msg_type == "vidio":
            pass
        elif msg_type == "location":
            pass
        elif msg_type == "link":
            pass
        elif msg_type == "event":
            event = request_xml.find("Event").text
            if event == "subscribe":
                return HttpResponse(self.find_reply(from_user_name, "用户关注事件"))
            elif event == "unsubscribe":
                return HttpResponse("Got it")
            elif event == "CLICK":
                event_key = request_xml.find("EventKey").text
                return HttpResponse(self.find_reply(from_user_name, event_key))
            elif event == "SCAN":
                pass
            elif event == "LOCATION":
                pass
            elif event == "VIEW":
                pass
        else:
            return HttpResponse(self.find_reply(from_user_name, "不支持的消息类型"))
        
    def parseXml(self, from_username, content):
        """根据content选择合适的回复 构造xml 返回
        """
        reply = Keyword.objects.filter(keyword=content)
        print str(reply[0].reply)
        if len(reply) > 1:
            reply = reply[random.randint(0, len(reply) - 1)]
        else:
            reply = reply[0]
    
        if reply.reply.reply_type == "text":
            return text_reply_xml(from_username, reply.reply.text_reply)
        elif reply.reply.reply_type == "voice":
            return voice_reply_xml(from_username, reply.reply.voice_reply)
        elif reply.reply.reply_type == "video":
            return video_reply_xml(from_username, reply.reply.video_reply)
        elif reply.reply.reply_type == "news":
            return news_reply_xml(from_username, reply.reply.news_reply.all())
        elif reply.reply.reply_type == "music":
            return music_reply_xml(from_username, reply.reply.music_title, reply.reply.music_description,
                                   reply.reply.music_url, reply.reply.music_hq_url)
        else:
            print u"错误的回复类型"
            
    def chinese_segment(self, content):
        _SEGMENT_BASE_URL = 'http://segment.sae.sina.com.cn/urlclient.php'
        payload = urllib.urlencode([('context', content.encode("utf-8")), ])
        args = urllib.urlencode([('word_tag', 1), ('encoding', 'UTF-8'), ])
        url = _SEGMENT_BASE_URL + '?' + args
        result = urllib2.urlopen(url, payload).read()
        return json.loads(result)
    
    
    def find_keyword(self, content):
        reply = Keyword.objects.filter(keyword=content)
        if len(reply):
            return True
        else:
            return False
    
    def find_reply(self, from_username, content):
        """查找文本消息是否有对应的回复  如果没有的话 进行中文分词 并再次判断
        """
        reply = find_keyword(content)
        if reply is False:
            # 直接查找没有找到对应的回复，这个时候对content进行中文分词
            segment_result = chinese_segment(content)
            segment_length = len(segment_result)
            while segment_length:
                segment_length -= 1
                content = segment_result[segment_length]["word"]
                reply = find_keyword(content)
                if reply is False:
                    continue
                else:
                    return parseXml(from_username, content)
            return parseXml(from_username, u"没有找到合适的回复")
        else:
            return parseXml(from_username, content)
    
    def createMenu(self, access_token, post_data):
        url = 'https://api.weixin.qq.com/cgi-bin/menu/create?access_token=%s' % (access_token)
        data = method_post_api(url, post_data)
        errcode = data.get("errcode")
        if errcode != 0:
            errmsg = data.get("errmsg")
            print '%s' , errmsg
        return errcode
    
    def deleteMenu(self, access_token):
        url = 'https://api.weixin.qq.com/cgi-bin/menu/delete?access_token=%s' % (access_token)
        data = method_get_api(url)
        errcode = data.get("errcode")
        return errcode
    
    def createGroup(self, access_token, post_data):
        url = 'https://api.weixin.qq.com/cgi-bin/groups/create?access_token=%s' % (access_token)
        data = method_post_api(url, post_data)
        gid = data["group"]["id"]
        gname = data["group"]["name"]
        if not gid:
            errcode = data.get("errcode")
            errmsg = data.get("errmsg")
            print '%s' , errmsg
            return errcode
        # write to database
            
    def getAllGroupInfo(self, access_token):
        url = 'https://api.weixin.qq.com/cgi-bin/groups/get?access_token=%s' % (access_token)
        data = method_get_api(url)
        list = data.get("group")
        list_len = len(list)
        if len == 0:
            return None
        for i in range(list_len):
            """list[i].get("id")
            list[i].get("name")
            list[i].get("count")
            write to db"""
            
    def getGroupidOfUser(self, access_token, openid):
        url = 'https://api.weixin.qq.com/cgi-bin/groups/getid?access_token=%s' % (access_token)
        post_data = {"openid":openid}
        data = method_post_api(url, post_data)
        gid = data.get("groupid")
        if not gid:
            errcode = data.get("errcode")
            errmsg = data.get("errmsg")
            print '%s' , errmsg
            return errcode
        return gid
    
    def changeGroupName(self, access_token, id, gname):
        url = 'https://api.weixin.qq.com/cgi-bin/groups/update?access_token=%s' % (access_token)
        post_data = {"group":{"id":id, "name":gname}}
        data = method_post_api(url, post_data)
        # write to db
        errcode = data.get("errcode")
        if errcode != 0:
            errmsg = data.get("errmsg")
            print '%s' , errmsg
            return errcode
        return errcode
    
    def getUserInfo(self, access_token, openid):
        url = 'https://api.weixin.qq.com/cgi-bin/user/info?access_token=%s&openid=%s&lang=zh_CN' % (access_token, openid)
        data = method_get_api(url)
        dict_len = len(data)
        if dict_len == 0:
            errcode = data.get("errcode")
            errmsg = data.get("errmsg")
            print '%s' , errmsg
            return errcode
        # write to db
        """
        data.get("subscribe")
        data.get("openid")
        data.get("nickname")
        data.get("sex")
        data.get("language")
        data.get("city")
        data.get("province")
        data.get("country")
        data.get("headimgurl")
        data.get("subscribe_time")
        data.get("unionid")
        """
        
    def getFucosUsers(self, access_token):
        """当用户超过10000时需要改动
        """
        url = 'https://api.weixin.qq.com/cgi-bin/user/get?access_token=%s&next_openid=None' % (access_token)
        # need ongoing

wxapi = WeixinInterface(WEIXIN_TOKEN, WEIXIN_APPID, WEIXIN_SECRET)

def weixin_main(request):
    """所有的消息都会先进入这个函数进行处理，函数包含两个功能，如果请求时get，
    说明是微信接入验证，如果是post就是微信正常的收发消息。
    """   
    global wxapi
    
    if request.method == "GET":
        return HttpResponse(wxapi.checkSignature(request))           
    else:
        xml_str = smart_str(request.body)
        request_xml = etree.fromstring(xml_str)
        response_xml = wxapi.auto_reply(request_xml)
        return HttpResponse(response_xml)
            
                
    
        
        
            

        
    
    
        
    
     
    
    
        
    
    
