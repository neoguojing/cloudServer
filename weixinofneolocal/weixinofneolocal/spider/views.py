# coding=utf-8
from django.utils.encoding import smart_str
from django.views.decorators.csrf import csrf_exempt
from lxml import etree
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
import threading
import thread 
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from interface.utils import *
from interface.weixinapi import WeixinInterface
from config.config import *
from interface.servctrl import *
from interface.models import *
from interface.xml_api import *
from interface.menu import *
# test
from interface.servctrl import *

@csrf_exempt
class NeoWeiXinServe:
    
    def __init__(self, token, appid, secret):
        self.sctrl = BasicCtrl()
        self.wxapi = WeixinInterface(token, appid, secret) 
        
    def doSysInit(self):
        errcode = 0
        errcode = self.wxapi.deleteMenu()
        errcode |= self.wxapi.createMenu()
        # errcode |= self.wxapi.createGroup("fuck")
        # chang jian fen zhu
        if errcode:
            return "NoOk"
        return "Ok"
    
    def syncServToLocal(self):
        self.wxapi.getAllGroupInfo()
        self.wxapi.getFucosUsersInfo()
       
    def processMsg(self, request_xml):
        """识别消息的类型 分类处理
        """
        # record msg
        # t_msgrecord = threading.Thread(target=self.wxapi.reccordMsg, name='msgrcd',args=(request_xml));
        # t_msgrecord.start();
        thread.start_new_thread(self.wxapi.reccordMsg, (request_xml,))

        msg_type = request_xml.find("MsgType").text
        from_user_name = request_xml.find("FromUserName").text
            
        if msg_type == "text":
            # return self.processText(request_xml, from_user_name);
            return self.processTextWithNews(request_xml, from_user_name);
        elif msg_type == "image":
            pass
        elif msg_type == "voice":
            pass
        elif msg_type == "video":
            pass
        elif msg_type == "location":
            self.processLocation(request_xml, from_user_name);
            # return self.wxapi.msgNotifyXmlApi(from_user_name, "subscribe");
            return self.wxapi.testMsgApi("location");
        elif msg_type == "link":
            pass
        elif msg_type == "event":
            return self.processEvent(request_xml, from_user_name)
        else:
            return self.wxapi.msgNotifyXmlApi(from_user_name);
            
    def processText(self, request_xml, to_userid):
        # TEST
        content = request_xml.find("Content").text
        rsp = self.sctrl.getRspText(content)
        return text_reply_xml(to_userid, rsp)
    
    def processTextWithNews(self, request_xml, to_userid):
        content = request_xml.find("Content").text
        rsp = self.sctrl.getRspNews(content)
        err_str = "There is no this service!"
        if rsp == None:
            text_reply_xml(to_userid, err_str)
        return news_reply_xml(to_userid, rsp)
    
    def processEvent(self, request_xml, to_userid):
        event = request_xml.find("Event").text
        if event == "subscribe":
            return self.processSubscribe(event, to_userid)
        elif event == "unsubscribe":
            return self.processUnSubscribe(event, to_userid)
        elif event == "CLICK":
            return self.processNews(request_xml, to_userid)
        elif event == "SCAN":
            pass
        elif event == "LOCATION":
            self.processLocation(request_xml, to_userid);
            # return self.wxapi.msgNotifyXmlApi(to_userid, "subscribe");
            return self.wxapi.testMsgApi("LOCATION");
        elif event == "VIEW":
            pass
        elif event == "location_select":
            self.processLocation(request_xml, to_userid);
            return self.wxapi.testMsgApi("location_select");
        elif event == "scancode_waitmsg":
            return self.processScanCode(request_xml, to_userid);
        elif event == "scancode_push":
            return self.processScanCode(request_xml, to_userid);
        elif event == "pic_sysphoto":
            pass
        elif event == "pic_photo_or_album":
            pass
        elif event == "pic_weixin":
            pass
        else:
            return self.wxapi.msgNotifyXmlApi(to_userid);

    # subsribe is dealed with text msg
    def processSubscribe(self, key, to_userid):
        # self.wxapi.getUserInfo(to_userid)
        return self.wxapi.msgNotifyXmlApi(to_userid, key);
    
    def processScanCode(self, request_xml, to_userid):
        self.sctrl.setScanCode(request_xml);
        tmp = request_xml.find("ScanCodeInfo");
        node = tmp.find('ScanResult').text;
        return text_reply_xml(to_userid, node);
    # views can not use sctrl directly
    def processNews(self, request_xml, to_userid):
        event_key = request_xml.find("EventKey").text
        rsp = self.sctrl.getRspNews(event_key)
        err_str = "There is no this service!"
        if rsp == None:
            text_reply_xml(to_userid, err_str)
        return news_reply_xml(to_userid, rsp)
        
    def processUnSubscribe(self, key, to_userid):
        rsp = self.sctrl.getRspText(key)
        return text_reply_xml(to_userid, rsp)
    
    def processLocation(self, request_xml, to_userid):
        # t_lctrcd = threading.Thread(target=self.wxapi.dealLocationMsg, name='lcdrcd', args=(request_xml));
        # t_lctrcd.start();
        thread.start_new_thread(self.wxapi.dealLocationMsg, (request_xml,))
        return;
        
wxserv = NeoWeiXinServe(WEIXIN_TOKEN, WEIXIN_APPID, WEIXIN_SECRET)
# util = WeixinUtil()

@csrf_exempt
def weixin_main(request):
    """所有的消息都会先进入这个函数进行处理，函数包含两个功能，如果请求时get，
    说明是微信接入验证，如果是post就是微信正常的收发消息。
    """   
#    log = util.method_get_log("app")
    if request.method == "GET":
        if wxserv.wxapi.isCodeRequest(request):
            
            # data = text_reply_json("okOD_suoJyb158onn-fox9HojiGc","Code gotten");
            # err = wxserv.wxapi.sendJsonMsg(data);
            # return HttpResponse(wxserv.wxapi.getUserCode(request));
            # return HttpResponse(wxserv.wxapi.getAuthToken(request), content_type="application/json");
            return HttpResponse(wxserv.wxapi.getAuthUserInfo(request), content_type="application/json");
        return HttpResponse(wxserv.wxapi.checkSignature(request));           
    else:
        xml_str = smart_str(request.body);
        # wxserv.sctrl.setRspText(xml_str);
#        log.info(xml_str)
        request_xml = etree.fromstring(xml_str);
#        log.info(request_xml)
        response_xml = wxserv.processMsg(request_xml);
#        log.info(response_xml)
        # return HttpResponse(response_xml, content_type="application/xml")
        return HttpResponse(response_xml)

@csrf_exempt
def SysInit(request):
    isok = wxserv.doSysInit()
    return HttpResponse(isok)

import string
def WeixinNews(request, key, index):
    bc = BasicCtrl();
    index = string.atoi(index);
    item = bc.getRspNewsItem(key, index);
    
    return render_to_response('weixin/news_display.html', {'picurl':item.pic_url, 'title': item.title, 'content': item.description}, context_instance=RequestContext(request));

def BootstrapTest(request):
    return render_to_response('bootstrap/button.html');   
    # return render_to_response('bootstrap/form.html'); 
    # return render_to_response('bootstrap/check.html'); 
    # return render_to_response('bootstrap/fuzhu.html'); 
    # return render_to_response('bootstrap/dropdown.html');
    # return render_to_response('bootstrap/nav.html');
	# return render_to_response('bootstrap/pagination.html');
    # return render_to_response('bootstrap/modal.html');
    # return render_to_response('bootstrap/hint.html');
    # return render_to_response('bootstrap/fold.html');
    # return render_to_response('bootstrap/carousel.html');
	# return render_to_response('bootstrap/scrollspy.html');

def AppMain(request):
    # return render_to_response('weixin/index.html',{},
        # context_instance=RequestContext(request, processors=[_app_main_context_proc]))
    return render_to_response('weixin/index.html', {},
        context_instance=RequestContext(request));
    
	    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
# test
html = u'''
<html>
<head>
    <title>Search</title>
</head>
<body>
    <form action="/myweixin/" method="post">
        <input type="text" name="q">
        <input type="submit" value="Search">
    </form>
</body>
</html>
'''

xml = u'''<xml><ToUserName><![CDATA[gh_e136c6e50636]]></ToUserName>
<FromUserName><![CDATA[oMgHVjngRipVsoxg6TuX3vz6glDg]]></FromUserName>
<CreateTime>1408090816</CreateTime>
<MsgType><![CDATA[event]]></MsgType>
<Event><![CDATA[pic_photo_or_album]]></Event>
<EventKey><![CDATA[6]]></EventKey>
<SendPicsInfo><Count>1</Count>
<PicList><item><PicMd5Sum><![CDATA[5a75aaca956d97be686719218f275c6b]]></PicMd5Sum>
</item>
</PicList>
</SendPicsInfo>
</xml>
 '''
location = '''<xml><ToUserName><![CDATA[gh_e136c6e50636]]></ToUserName>
<FromUserName><![CDATA[oMgHVjngRipVsoxg6TuX3vz6glDg]]></FromUserName>
<CreateTime>1408091189</CreateTime>
<MsgType><![CDATA[event]]></MsgType>
<Event><![CDATA[location_select]]></Event>
<EventKey><![CDATA[6]]></EventKey>
<SendLocationInfo><Location_X><![CDATA[23]]></Location_X>
<Location_Y><![CDATA[113]]></Location_Y>
<Scale><![CDATA[15]]></Scale>
<Label><![CDATA[ 广州市海珠区客村艺苑路 106号]]></Label>
<Poiname><![CDATA[]]></Poiname>
</SendLocationInfo>
</xml>
'''
neo = 'okOD_suoJyb158onn-fox9HojiGc'
cao = u"发送位置"
url = 'https://api.weixin.qq.com/cgi-bin/groups/create?access_token=%s' % (wxserv.wxapi.get_access_token())
group = {"group": {"name": "client"}}
sc = BasicCtrl()
ut = WeixinUtil()
image = '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'
from config.settings import ROOT_PATH
from utils.sae_storage import *
from django.http import HttpResponseRedirect
import base64
def test(request):
    # return wxapi.doUserAuth()
    # data = sc.getRspText(1)
    # request_xml = etree.fromstring(xml)
    # content = request_xml.find("Content").text
    # return HttpResponse(text_reply_xml())
    # access token test
    # return HttpResponse(wxserv.wxapi.get_access_token())
    # wxserv.doSysInit()
    # rsp = sc.getRspNews("news_push")
    # return HttpResponse(rsp)
    # return HttpResponse(wxserv.wxapi.getFucosUsersInfo(),content_type="application/json")
    # return HttpResponse(wxserv.wxapi.createMenu())
    # return HttpResponse(wxserv.wxapi.getAllGroupInfo(),content_type="application/json")
    # return HttpResponse(wxserv.wxapi.msgNotifyApi("okOD_suoJyb158onn-fox9HojiGc",'news'));
	# return HttpResponse(wxserv.wxapi.notifyToAll('news'));
    # return HttpResponse(wxserv.wxapi.downloadFile('MO7HQ1RKQrsFoWgEiL6p1xzOoNrQ8w64jgGUgoE4eeao7BJgG4_64cVsRhRWQuvC',ROOT_PATH+'app/static/image/test.jpg'));
    # data = wxserv.sctrl.getMediaMsg('MO7HQ1RKQrsFoWgEiL6p1xzOoNrQ8w64jgGUgoE4eeao7BJgG4_64cVsRhRWQuvC',ROOT_PATH+'app/static/image/test.jpg');
    # data1 = data.filefd
    # decode = base64.b64decode(data1)
    # decode = base64.b64decode(image)
    # return HttpResponse(setToSAEStorage('image/test.jpg',decode));
	# return HttpResponse(wxserv.wxapi.uploadFile('image',ROOT_PATH+'app/static/image/2006419181421600.jpg'),content_type="application/json");
	# return HttpResponse(wxserv.sctrl.getAllUserInfo());
    # return HttpResponse(wxserv.sctrl.setLocationInfo(etree.fromstring(location)));
    # t_msgrecord = threading.Thread(target=wxserv.wxapi.reccordMsg, name='msgrcd',args=(etree.fromstring(location)));
    # t_msgrecord.start();
    # thread.start_new_thread(wxserv.wxapi.reccordMsg, (etree.fromstring(location),)) 
    # return HttpResponse(t_msgrecord);
    # return HttpResponse(wxserv.wxapi.reccordMsg(etree.fromstring(xml)));
    # return HttpResponse(text_reply_xml(neo, wxserv.sctrl.getScanCode(neo).scanresult));
    # data = wxserv.wxapi.createTmpScanCode(1);
    # return HttpResponse(data);
    # return HttpResponse(setToSAEStorage("scan.jpg",wxserv.wxapi.getScanCodePic(data)),'image');
    return HttpResponseRedirect('http://weixinofneo-media.stor.sinaapp.com/image/Capture.PNG');
    # return HttpResponse(wxserv.wxapi.msgNotifyApi('okOD_suoJyb158onn-fox9HojiGc', 'subscribe'));
    # return HttpResponse(wxserv.wxapi.sendJsonMsg(text_reply_json("okOD_suoJyb158onn-fox9HojiGc",cao)));
    # return HttpResponse(wxserv.sctrl.setRspText("草"));
    # return HttpResponse(text_reply_json("okOD_suoJyb158onn-fox9HojiGc","hello, word"),content_type="application/json")
    # return HttpResponse(wxserv.wxapi.getUserInfo("okOD_suoJyb158onn-fox9HojiGc"))
    # return HttpResponse(ut.method_post_api(url, group))
    # return HttpResponse(news_reply_xml("userid", rsp))
    # return HttpResponse(news_reply_xml("userid", rsp), content_type="application/xml")
    
