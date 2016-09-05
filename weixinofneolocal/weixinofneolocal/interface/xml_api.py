# coding=utf-8
import urllib2
import time
import random
from config.config import WEIXIN_ID



def text_reply_json(openid, text):
   
    json_data = u'''
    {
        "touser":"%s",
        "msgtype":"text",
        "text":
        {
             "content":"%s"
        }
    }''' % (openid, text)
    return json_data

def image_reply_json(openid, mediaid):
    json_data = u'''
    {
        "touser":"%s",
        "msgtype":"image",
        "image":
        {
          "media_id":"%s"
        }
    }''' % (openid, mediaid)
    return json_data
    
def voice_reply_json(openid, mediaid):
    json_data = u'''
    {
        "touser":"%s",
        "msgtype":"voice",
        "voice":
        {
          "media_id":"%s"
        }
    }''' % (openid, mediaid)
    return json_data

def video_reply_json(openid, mediaid1, mediaid2, title, desc):
    json_data = u'''
    {
        "touser":"%s",
        "msgtype":"video",
        "video":
        {
          "media_id":"%s",
          "thumb_media_id":"%s",
          "title":"%s",
          "description":"%s"
        }
    }
    ''' % (openid, mediaid1, mediaid2, title , desc)
    return json_data
    
def music_reply_json(openid, title, desc, url, hurl , mediaid):
    json_data = u'''
    {
        "touser":"%s",
        "msgtype":"music",
        "music":
        {
          "title":"%s",
          "description":"%s",
          "musicurl":"%s",
          "hqmusicurl":"%s",
          "thumb_media_id":"%s"
        }
    }
    ''' % (openid, title, desc, url , hurl, mediaid)
    return json_data
    
def news_reply_json(to_username, news):
    news_num = len(news)
    xml = u"""
    {
        "touser":"%s",
        "msgtype":"news",
        "news":{
            "articles": [
        """ % (to_username)
    num = news_num
    for num in range(0, news_num):
        item_xml = u"""
                  {
                      "title":"%s",
                      "description":"%s",
                      "url":"%s",
                      "picurl":"%s"
                  },
               """ % (news[num].title, news[num].description, news[num].pic_url, news[num].url)
        xml += item_xml

    xml += u"""
                    ]
                }
            }
           """
    return xml

def text_reply_xml(to_username, in_text):
    """构造文本回复的xml
    ToUserName	 是	 接收方帐号（收到的OpenID）
	FromUserName	 是	开发者微信号
	CreateTime	 是	 消息创建时间 （整型）
	MsgType	 是	 text
	Content	 是	 回复的消息内容（换行：在content中能够换行，微信客户端就支持换行显示）
    """
    xml = u"""
            <xml>
            <ToUserName><![CDATA[%s]]></ToUserName>
            <FromUserName><![CDATA[%s]]></FromUserName>
            <CreateTime>%s</CreateTime>
            <MsgType><![CDATA[text]]></MsgType>
            <Content><![CDATA[%s]]></Content>
            </xml>""" % (to_username, WEIXIN_ID, str(int(time.time())), in_text)
    return xml

def image_reply_xml(to_username, mediaid):
    """ToUserName	 是	 接收方帐号（收到的OpenID）
	FromUserName	 是	开发者微信号
	CreateTime	 是	 消息创建时间 （整型）
	MsgType	 是	 image
	MediaId	 是	 通过上传多媒体文件，得到的id。
    """
    xml = u"""
            <xml>
	<ToUserName><![CDATA[%s]]></ToUserName>
	<FromUserName><![CDATA[%s]]></FromUserName>
	<CreateTime>%s</CreateTime>
	<MsgType><![CDATA[image]]></MsgType>
	<Image>
	<MediaId><![CDATA[%s]]></MediaId>
	</Image>
	</xml>""" % (to_username, WEIXIN_ID, str(int(time.time())), mediaid)
    return xml

def voice_reply_xml(to_username, voiceid):
    """ToUserName	 是	 接收方帐号（收到的OpenID）
	FromUserName	 是	开发者微信号
	CreateTime	 是	 消息创建时间戳 （整型）
	MsgType	 是	 语音，voice
	MediaId	 是	 通过上传多媒体文件，得到的id
    """
    xml = u"""
     <xml>
	<ToUserName><![CDATA[%s]]></ToUserName>
	<FromUserName><![CDATA[%s]]></FromUserName>
	<CreateTime>%s</CreateTime>
	<MsgType><![CDATA[voice]]></MsgType>
	<Voice>
	<MediaId><![CDATA[%s]]></MediaId>
	</Voice>
	</xml>""" % (to_username, WEIXIN_ID, str(int(time.time())), voiceid)
    return xml

def video_reply_xml(to_username, videoid, title, desc):
    """ToUserName	 是	 接收方帐号（收到的OpenID）
	FromUserName	 是	开发者微信号
	CreateTime	 是	 消息创建时间戳 （整型）
	MsgType	 是	 语音，voice
	MediaId	 是	 通过上传多媒体文件，得到的id
    """
    xml = u"""
          <xml>
	<ToUserName><![CDATA[%s]]></ToUserName>
	<FromUserName><![CDATA[%s]]></FromUserName>
	<CreateTime>%s</CreateTime>
	<MsgType><![CDATA[video]]></MsgType>
	<Video>
	<MediaId><![CDATA[%s]]></MediaId>
	<Title><![CDATA[%s]]></Title>
	<Description><![CDATA[%s]]></Description>
	</Video> 
	</xml>""" % (to_username, WEIXIN_ID, str(int(time.time())), videoid, title, desc)
    return xml

def music_reply_xml(to_username, title, description, music_url, hq_music_url):
    """构造音乐回复的xml
    ToUserName	 是	 接收方帐号（收到的OpenID）
	FromUserName	 是	开发者微信号
	CreateTime	 是	 消息创建时间 （整型）
	MsgType	 是	 music
	Title	 否	 音乐标题
	Description	 否	 音乐描述
	MusicURL	 否	 音乐链接
	HQMusicUrl	 否	 高质量音乐链接，WIFI环境优先使用该链接播放音乐
	ThumbMediaId	 是	 缩略图的媒体id，通过上传多媒体文件，得到的id
    """
    xml = u"""
            <xml>
            <ToUserName><![CDATA[%s]]></ToUserName>
            <FromUserName><![CDATA[%s]]></FromUserName>
            <CreateTime>%s</CreateTime>
            <MsgType><![CDATA[music]]></MsgType>
            <Music>
            <Title><![CDATA[%s]]></Title>
            <Description><![CDATA[%s]]></Description>
            <MusicUrl><![CDATA[%s]]></MusicUrl>
            <HQMusicUrl><![CDATA[%s]]></HQMusicUrl>
            </Music>
            </xml>
            """ % (to_username, WEIXIN_ID, str(int(time.time())), title, description, music_url, hq_music_url)
    return xml


def news_reply_xml(to_username, news):
    """
    ToUserName	 是	 接收方帐号（收到的OpenID）
	FromUserName	 是	开发者微信号
	CreateTime	 是	 消息创建时间 （整型）
	MsgType	 是	 news
	ArticleCount	 是	 图文消息个数，限制为10条以内
	Articles	 是	 多条图文消息信息，默认第一个item为大图,注意，如果图文数超过10，则将会无响应
	Title	 否	 图文消息标题
	Description	 否	 图文消息描述
	PicUrl	 否	 图片链接，支持JPG、PNG格式，较好的效果为大图360*200，小图200*200
	Url	 否	 点击图文消息跳转链接
    """
    news_num = len(news)
    xml = u"""
            <xml>
            <ToUserName><![CDATA[%s]]></ToUserName>
            <FromUserName><![CDATA[%s]]></FromUserName>
            <CreateTime>%s</CreateTime>
            <MsgType><![CDATA[news]]></MsgType>
            <ArticleCount>%s</ArticleCount>
            <Articles>
        """ % (to_username, WEIXIN_ID, str(int(time.time())), news_num)
    num = news_num
    for num in range(0, news_num):
        item_xml = u"""
                   <item>
                   <Title><![CDATA[%s]]></Title>
                   <Description><![CDATA[%s]]></Description>
                   <PicUrl><![CDATA[%s]]></PicUrl>
                   <Url><![CDATA[%s]]></Url>
                   </item>
               """ % (news[num].title, news[num].description, news[num].pic_url, news[num].url)
        xml += item_xml

    xml += u"""
             </Articles>
             </xml>
           """
    return xml
