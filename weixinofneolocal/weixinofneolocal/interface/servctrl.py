# -*- coding: utf-8 -*-
# coding=utf-8
"""
Created on Sat Nov  8 17:02:33 2014

@author: root
use database to complete business control
"""
# import string
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from interface.models import *
from interface.xml_api import *

class BasicCtrl():
    def __init__(self):
        pass
    
    def saveUserInfo(self):
        pass
    
    def getRspText(self, in_key):
        objdict = TextMsg.objects.filter(key=in_key, isactive=True)
        if len(objdict) == 0:
            return "There is no this service!"
        return objdict[0].text
    
    def setRspText(self, data, in_key=time.ctime(), active=False):
        m_text = TextMsg(key=in_key, isactive=active, text=data.encode('utf-8'));
        m_text.save();
        return m_text;
    
    def getRspNews(self, in_key):
        newsdict = News.objects.filter(key=in_key, isactive=True)
        if len(newsdict) == 0:
            return None
        # itemdict = newsdict.item_set.all()
        itemdict = ItemOfNews.objects.filter(item=newsdict[0].key)
        if len(itemdict) == 0:
            return None
        return itemdict
    
    def getRspNewsItem(self, in_key, index=0):
        objdict = self.getRspNews(in_key);
        if objdict == None:
            return None;
        return objdict[index];
        
    
    def getRspImage(self, in_key):
        pass;
    
    def getRspVoice(self, in_key):
        pass;
    
    def getRspMusic(self, in_key):
        pass;
    
    def getRspVideo(self, in_key):
        pass;
    
    
    def isUserExist(self, openid):
        objdict = WeiXinUsers.objects.filter(userid=openid)
        if len(objdict) == 0:
            return False
        return True
    
    def setUserInfo(self, in_req, g_id):
        if  in_req.get("subscribe") == 1:
            m_subscrib = True
        else:
            m_subscrib = False
        
        if  in_req.get("sex") == 1:
            m_sex = True
        else:
            m_sex = False
        
        m_subtime = in_req.get("subscribe_time");
        if m_subtime == None:
            m_subtime = 0;
        
        # m_gp = WeiXinGroups.objects.filter(gid=0)
        m_user = WeiXinUsers(issubscribe=m_subscrib, userid=in_req.get("openid").\
        encode('utf-8'), gid_id=g_id, nickname=in_req.get("nickname").encode('utf-8'), \
        sex=m_sex , city=in_req.get("city").encode('utf-8'), country=in_req.\
        get("country").encode('utf-8'), province=in_req.get("province").encode('utf-8'), \
        language=in_req.get("language").encode('utf-8'), headimgurl=in_req.get("headimgurl").\
        encode('utf-8'), subscribe_time=m_subtime)
        # unionid=in_req.get("unionid")
        # tianjia wai jian
        # m_user.gid.add(m_gp)
        m_user.save()
        
        return 0
    
    def getAllUserInfo(self):
        userlist = WeiXinUsers.objects.all();
        return userlist;
        
    def setUserInfoTest(self, openid):     
        # m_gp = WeiXinGroups.objects.filter(gid=0)    
        # m_user.gid.add(m_gp)
        m_user = WeiXinGroups(gid=27, gname=openid.encode('utf-8'), count=1)
        # tianjia wai jianue
        
        m_user.save()
        
    def isGroupExist(self, g_id):
        objdict = WeiXinGroups.objects.filter(gid=g_id)
        if len(objdict) == 0:
            return False
        return True
    
    def setGroupInfo(self, gid, gname, count):
        m_group = WeiXinGroups(gid=gid, gname=gname.encode('utf-8'), count=count)
        m_group.save()
    
    def setLocationInfo(self, xml_req):
        
        m_msgid = xml_req.find("MsgId");
        if m_msgid == None:
            m_msgid = 0;
        else:
            m_msgid = m_msgid.text;
        
        tmp = xml_req.find("SendLocationInfo");
        if None == tmp:
            child = xml_req;
        else:
            child = tmp;
            
        m_latitude = child.find("Location_X");
        if m_latitude == None:
            m_latitude = child.find("Latitude").text;
        else:
            m_latitude = m_latitude.text;
            
        m_longitude = child.find("Location_Y");
        if m_longitude == None:
            m_longitude = child.find("Longitude").text;
        else:
            m_longitude = m_longitude.text;
            
        m_scale = child.find("Scale");
        if m_scale == None:
            m_scale = 0;
        else:
            m_scale = m_scale.text;
            
        m_label = child.find("Label");
        if m_label == None:
            m_label = '';
        else:
            m_label = m_label.text;
        
        m_prec = xml_req.find("Precision");
        if m_prec == None:
            m_prec = 0;
        else:
            m_prec = m_prec.text;
            
        m_locate = LocationOfUser(msgtime=xml_req.find("CreateTime").text\
        , userid_id=xml_req.find("FromUserName").text\
        , msgid=m_msgid, latitude=m_latitude, longitude=m_longitude\
        , precision=m_prec, scale=m_scale, lable=m_label);
        m_locate.save();
        return m_locate;
    
    def getNumXmlNode(self, xml_req, nodename):
        node = xml_req.find(nodename);
        if node == None:
            node = 0;
        else:
            node = node.text;
        return node;
    
    def getStrXmlNode(self, xml_req, nodename):
        node = xml_req.find(nodename);
        if node == None:
            node = '';
        else:
            node = node.text;
        return node;
    
    def setMsgRecord(self, xml_req):
        m_msgid = xml_req.find("MsgId");
        if m_msgid == None:
            m_msgid = 0;
        else:
            m_msgid = m_msgid.text;
        
        m_content = xml_req.find("Description");
        if m_content == None:
            m_content = xml_req.find("Content");
            if m_content != None:
                m_content = m_content.text;
            else:
                m_content = '';
        else:
        	m_content = m_content.text;
        
        m_event = xml_req.find("Event");
        if m_event == None:
            m_event = '';
        else:
            m_event = m_event.text;
        
        m_eventkey = xml_req.find("EventKey");
        if m_eventkey == None:
            m_eventkey = '';
        else:
            m_eventkey = m_eventkey.text;
            
        m_title = xml_req.find("Title");
        if m_title == None:
            m_title = '';
        else:
            m_title = m_title.text;
        
        m_url = xml_req.find("Url");
        if m_url == None:
            m_url = '';
        else:
            m_url = m_url.text;
        
        m_mediaid = xml_req.find("MediaId");
        if m_mediaid == None:
            m_mediaid = '';
        else:
            m_mediaid = m_mediaid.text;
        
        m_tmediaid = xml_req.find("ThumbMediaId");
        if m_tmediaid == None:
            m_tmediaid = '';
        else:
            m_tmediaid = m_tmediaid.text;
        
        tmp = xml_req.find("SendLocationInfo");
        if None == tmp:
            child = xml_req;
        else:
            child = tmp;
        
        m_picount = child.find("Count");
        if m_picount == None:
            m_picount = 0;
        else:
            m_picount = m_picount.text;
        
        tmp = child.find("PicList");
        if None == tmp:
            child1 = xml_req;
        else:
            child1 = tmp;
            
        tmp = child1.find("item");
        if None == tmp:
            child2 = xml_req;
        else:
            child2 = tmp;
        
        m_picmd5 = child2.find("PicMd5Sum");
        if None == m_picmd5:
            m_picmd5 = '';
        else:
            m_picmd5 = m_picmd5.text;
               
        m_msgrcd = MsgRecord(msgid=m_msgid\
        , msgtime=xml_req.find("CreateTime").text\
        , userid_id=xml_req.find("FromUserName").text.encode('utf-8')\
        , msgtype=xml_req.find("MsgType").text, event=m_event, eventkey=m_eventkey\
        , title=m_title, content=m_content, url=m_url, mediaid=m_mediaid\
        , thumediaid=m_tmediaid, picount=m_picount, picmd5=m_picmd5);
         
        m_msgrcd.save();
        return xml_req;
        
    def setMediaMsg(self, mediaid, filedata):
        m_mediamsg = MediaMsg(key='test', userid_id='okOD_suoJyb158onn-fox9HojiGc', msgtype='test', isactive=False, mediaid=mediaid, filefd=filedata);
        m_mediamsg.save();
        return m_mediamsg;
    
    def getMediaMsg(self, mediaid, filedata):
        objdict = MediaMsg.objects.filter(key='test');
        if len(objdict) == 0:
            return "There is no this data!"
        return objdict[0];
        
    def setScanCode(self, xml_req):
        m_event = self.getStrXmlNode(xml_req, "Event");
        m_eventkey = self.getStrXmlNode(xml_req, "EventKey");
        m_ticket = self.getStrXmlNode(xml_req, "Ticket");
        
        tmp = xml_req.find("ScanCodeInfo");
        if None == tmp:
            child = xml_req;
        else:
            child = tmp;
        m_scantype = self.getStrXmlNode(child, "ScanType");
        m_scanresult = self.getStrXmlNode(child, "ScanResult");
               
        m_scancode = ScanCode(msgtime=xml_req.find("CreateTime").text\
        , userid_id=xml_req.find("FromUserName").text.encode('utf-8')\
        , msgtype=xml_req.find("MsgType").text, event=m_event, eventkey=m_eventkey\
        , scantype=m_scantype, scanresult=m_scanresult, tickit=m_ticket);
         
        m_scancode.save();
        return xml_req;
    
    def getScanCode(self, key):
        objdict = ScanCode.objects.filter(userid_id=key);
        if len(objdict) == 0:
            return "There is no this data!"
        return objdict[0];
        
        
        
