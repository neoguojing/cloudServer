# -*- coding: utf-8 -*-
#coding=utf-8

# pls set the filed as '', if the filed has no a valid value

def get_verify_json(code):
    json_data=u'''
    {"code":"%s"}
    ''' % (code)
    return json_data
    
register_datacheck_json=u'''
    {"step":"1","phone":"1232@163.com","username":"12345678901","password":"123456"}
'''

register_json=u'''
    {"step":"6","username":"test3", "first_name":"","last_name":"","email":"",
    "password":"123456","is_staff":"0", "is_active":"1","phone": "+8614785236901","gender":"0",
    "birthday":"2016-09-14","constellation":"","vip":"0","grouprole":"0","industry":"IT",
    "device":"0","multipic":"0"}
'''

login_json=u'''
    {"username":"test","email":"1232@163.com","phone":"12345678901","password":"123456"}
'''


user=u'''
    {
        "username":"%s", "first_name":"%s","last_name":"%s","email":"%s","password":"%s","is_staff":"0", "is_active":"%s",
    }
'''

profile=u'''
    {
        "name":"%s" ,"userid":"%s","phone": "%s","gender":"%s","birthday":"%s","constellation":"%s",
         "vip":"%s","grouprole":"%s","industry":"%s","device":"%s","multipic":"%s",
    }
'''

userphotos=u'''
    {
        "name":"%s" ,"userid":"%s","info": "%s"
    }
'''

location=u'''
    {
        "name":"%s" ,"userid":"%s","latitude": "%s","longitude":"%s","info":"%s",
    }
'''

signature=u'''
    {
        "name":"%s" ,"userid":"%s","sign": "%s",
    }
'''

relation=u'''
    {
        "name":"%s" ,"userid":"%s","frendid": "%s","relation":"%s",
'''

status=u'''
    {
        "name":"%s" ,"userid":"%s","content": "%s","content_count":"%s"
    }
'''

apps=u'''
    {
        "name":"%s" ,"userid":"%s","sina": "%s","weixin":"%s",renren":"%s","fb":"%s","google":"%s",
         "twitter":"%s",
    }
'''

NOERROR = u'''{
    "errcode":"0",
    "info":"no error"
    }'''

REGISTER_SUCCESS = u'''{
    "errcode":"1",
    "info":"register success"
    }'''
    
REGISTER_USER_EXIST = u'''{
    "errcode":"2",
    "info":"register user exist"
    }'''

USER_NOEXIST = u'''{
    "errcode":"3",
    "info":"user not exist"
    }'''
    
LOGIN_SUCCESS = u'''{
    "errcode":"4",
    "info":"user login success"
    }'''
    
PASSWORD_INVALICE = u'''{
    "errcode":"5",
    "info":"password wrong"
    }'''

PASSWORD_ISNONE = u'''{
    "errcode":"6",
    "info":"need password"
    }'''

PHONE_NOEXIST = u'''{
    "errcode":"7",
    "info":"phone not exist"
    }'''

EMAIL_NOEXIST = u'''{
    "errcode":8,
    "info":"email not exist"
    }'''
    
INVALIDE_JSON = u'''{
    "errcode":"9",
    "info":"invalid json data"
    }'''
    
UERE_LOGOUT = u'''{
    "errcode":"10",
    "info":"user logout"
    }'''

UER_NOLOGIN = u'''{
    "errcode":"11",
    "info":"user has not loged in"
    }'''
    
DATA_NOEXIST = u'''{
    "errcode":"12",
    "info":"user data do not exist"
    }'''

PHONE_REGISTERED = u'''{
    "errcode":"13",
    "info":"phone has been register"
    }'''
    
PIC_UPLOAD_FAILED = u'''{
    "errcode":"14",
    "info":"image upload failed"
    }'''
    
PIC_DOWNLOAD_ERROR = u'''{
    "errcode":"15",
    "info":"file path is empty"
    }'''