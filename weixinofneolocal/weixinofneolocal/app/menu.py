# -*- coding: utf-8 -*-
# coding=utf-8
"""
Created on Thu Nov  6 21:19:59 2014

@author: root
"""


app_menu = u'''{"button":[\
{"name":"发送位置","type":"location_select","key": "rselfmenu_2_0"},\
{"name":"消息回复","sub_button":[{"type":"view","name":"登陆","url":"http://weixinofneo.sinaapp.com/admin/"},{"type":"click","name":"新闻","key":"news_push"},\
{"type":"click","name":"图片","key":"pic_push"},{"type":"click","name":"语音","key":"voice_push"},{"type":"click","name":"视频","key":"media_push"}]},\
{"name":"扫码发图","sub_button":[{"type":"scancode_waitmsg","name":"扫码提示","key":"rselfmenu_0_0","sub_button":[]},{"type":"scancode_push","name":"扫码事件","key":"rselfmenu_0_1","sub_button":[]},\
{"type":"pic_sysphoto","name":"拍照发图","key":"rselfmenu_1_0","sub_button":[]},{"type":"pic_photo_or_album","name":"混合发图","key":"rselfmenu_1_1","sub_button":[]},\
{ "type":"pic_weixin","name":"相册发图","key":"rselfmenu_1_2","sub_button":[]}]}]}'''

app_menu0 = '''{"button":[{"name":"发送位置","type":"location_select","key": "rselfmenu_2_0"},{"name":"消息回复","sub_button":[{"type":"view","name":"登陆","url":"http://weixinofneo.sinaapp.com/admin/"},{"type":"click","name":"新闻","key":"news_push"},{"type":"click","name":"图片","key":"pic_push"},{"type":"click","name":"语音","key":"voice_push"},{"type":"click","name":"视频","key":"media_push"}]},{"name":"扫码发图","sub_button":[{"type":"scancode_waitmsg","name":"扫码提示","key":"rselfmenu_0_0","sub_button":[]},{"type":"scancode_push","name":"扫码事件","key":"rselfmenu_0_1","sub_button":[]},{"type":"pic_sysphoto","name":"拍照发图","key":"rselfmenu_1_0","sub_button":[]},{"type":"pic_photo_or_album","name":"混合发图","key":"rselfmenu_1_1","sub_button":[]},{ "type":"pic_weixin","name":"相册发图","key":"rselfmenu_1_2","sub_button":[]}]}]}'''

app_menu1 = u'''{
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
                    "name": "扫码提示",
                    "key": "rselfmenu_0_0"
                },
                {
                    "type": "scancode_push",
                    "name": "扫码事件",
                    "key": "rselfmenu_0_1"
                },
                {
                    "type": "pic_sysphoto",
                    "name": "拍照发图",
                    "key": "rselfmenu_1_0",
                    "sub_button": [ ]
                },
                {
                    "type": "pic_photo_or_album",
                    "name": "混合发图",
                    "key": "rselfmenu_1_1"
                },
                {
                    "type": "pic_weixin",
                    "name": "相册发图",
                    "key": "rselfmenu_1_2"
                }
            ]
        }
    ]
}'''

app_menu2 = u'''{
    "button": [
        {
            "name": "发送位置",
            "type": "location_select",
            "key": "rselfmenu_2_0"
        },
        {
            "name": "基本功能",
            "sub_button": [
                {
                    "type": "view",
                    "name": "登陆",
                    "url": "http://weixinofneo.sinaapp.com/admin/"
                },
                {
                    "type": "view",
                    "name": "论坛",
                    "url": "http://weixinofneo.sinaapp.com/neoforum/"
                },
                {
                    "type": "view",
                    "name": "博客",
                    "url": "http://weixinofneo.sinaapp.com/weblog/"
                },
                {
                    "type": "view",
                    "name": "网店系统",
                    "url": "http://weixinofneo.sinaapp.com/store/"
                },
                {
                    "type": "click",
                    "name": "用户授权",
                    "key": "news_push"
                }
            ]
        },
        {
            "name": "微信小店",
            "sub_button": [
                {
                    "type": "scancode_waitmsg",
                    "name": "扫码提示",
                    "key": "rselfmenu_0_0",
                    "sub_button": [ ]
                },
                {
                    "type": "scancode_push",
                    "name": "扫码事件",
                    "key": "rselfmenu_0_1",
                    "sub_button": [ ]
                }
            ]
        }
    ]
}'''

app_menu4 = u'''{
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
                }
            ]
        },
        {
            "name": "扫码发图",
            "sub_button": [
                {
                    "type": "scancode_waitmsg",
                    "name": "扫码提示",
                    "key": "rselfmenu_0_0",
                    "sub_button": [ ]
                },
                {
                    "type": "scancode_push",
                    "name": "扫码事件",
                    "key": "rselfmenu_0_1",
                    "sub_button": [ ]
                }
            ]
        }
    ]
}'''

cjyx = u'''{
    "button": [
        {
            "name": "主页",
            "type": "view",
            "url": "http://weixinofneo.sinaapp.com/app/"
        },
        {
            "name": "基本功能",
            "sub_button": [
                {
                    "type": "view",
                    "name": "登陆",
                    "url": "http://weixinofneo.sinaapp.com/admin/"
                },
                {
                    "type": "view",
                    "name": "论坛",
                    "url": "http://weixinofneo.sinaapp.com/neoforum/"
                },
                {
                    "type": "view",
                    "name": "博客",
                    "url": "http://weixinofneo.sinaapp.com/weblog/"
                },
                {
                    "type": "view",
                    "name": "网店系统",
                    "url": "http://weixinofneo.sinaapp.com/store/"
                },
                {
                    "type": "click",
                    "name": "用户授权",
                    "key": "news_push"
                }
            ]
        },
        {
            "name": "微信小店",
            "sub_button": [
                {
                    "type": "scancode_waitmsg",
                    "name": "扫码提示",
                    "key": "rselfmenu_0_0",
                    "sub_button": [ ]
                },
                {
                    "type": "scancode_push",
                    "name": "扫码事件",
                    "key": "rselfmenu_0_1",
                    "sub_button": [ ]
                }
            ]
        }
    ]
}'''
