# coding=utf-8

my_menu = {
    "button":[
    {	
         "type":"click",
         "name":"今日歌曲",
         "key":"V1001_TODAY_MUSIC"
     },
     {
          "name":"菜单",
          "sub_button":[
          {	
              "type":"view",
              "name":"搜索",
              "url":"http://www.soso.com/"
           },
           {
              "type":"view",
              "name":"视频",
              "url":"http://v.qq.com/"
           },
           {
              "type":"click",
              "name":"赞一下我们",
              "key":"V1001_GOOD"
           }]
      }]
}

def group_patten(g_name):
    group = u"""{"group":{"name":"%s"}}
    """ % g_name
    return group

my_menu1 = {
    "button": [
        {
            "name": "发送位置",
            "type": "location_select",
            "key": "rselfmenu_2_0"
        },
        {
            "name": "消息回复",
            "sub_button": [
                {
                    "type": "view",
                    "name": "登陆",
                    "url": "http://weixinofneo.sinaapp.com/admin/"
                },
                {
                    "type": "click",
                    "name": "新闻",
                    "key": "news_push"
                },
                {
                    "type": "click",
                    "name": "音乐",
                    "key": "music_push"
                },
                {
                    "type": "click",
                    "name": "图片",
                    "key": "pic_push"
                },
                {
                    "type": "click",
                    "name": "语音",
                    "key": "voice_push"
                },
                {
                    "type": "click",
                    "name": "视频",
                    "key": "media_push"
                }
            ]
        },
        {
            "name": "扫码发图",
            "sub_button": [
                {
                    "type": "scancode_waitmsg",
                    "name": "扫码带提示",
                    "key": "rselfmenu_0_0",
                    "sub_button": [ ]
                },
                {
                    "type": "scancode_push",
                    "name": "扫码推事件",
                    "key": "rselfmenu_0_1",
                    "sub_button": [ ]
                },
                {
                    "type": "pic_sysphoto",
                    "name": "系统拍照发图",
                    "key": "rselfmenu_1_0",
                    "sub_button": [ ]
                },
                {
                    "type": "pic_photo_or_album",
                    "name": "拍照或者相册发图",
                    "key": "rselfmenu_1_1",
                    "sub_button": [ ]
                },
                {
                    "type": "pic_weixin",
                    "name": "微信相册发图",
                    "key": "rselfmenu_1_2",
                    "sub_button": [ ]
                }
            ]
        }
    ]
}
