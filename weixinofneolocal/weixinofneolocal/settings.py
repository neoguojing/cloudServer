#coding=utf-8

# pls set the filed as '', if the filed has no a valid value

login=u'''
    {
        "username":"%s","email":"%s","phone":"%s","password":"%s",
    }
'''


user=u'''
    {
        "username":"%s", "first_name":"%s","last_name":"%s","email":"%s","password":"%s","is_staff":"%s", "is_active":"%s",
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

REGISTER_SUCCESS = u'''{
    "errcode":1,
    "info":"register success"
    }'''
    
REGISTER_USER_EXIST = u'''{
    "errcode":2,
    "info":"register user exist"
    }'''

USER_NOEXIST = u'''{
    "errcode":3,
    "info":"user not exist"
    }'''
    
LOGIN_SUCCESS = u'''{
    "errcode":4,
    "info":"user login success"
    }'''
    
PASSWORD_INVALICE = u'''{
    "errcode":5,
    "info":"password wrong"
    }'''

PASSWORD_ISNONE = u'''{
    "errcode":6,
    "info":"need password"
    }'''

PHONE_NOEXIST = u'''{
    "errcode":7,
    "info":"phone not exist"
    }'''

EMAIL_NOEXIST = u'''{
    "errcode":8,
    "info":"email not exist"
    }'''
    
INVALIDE_JSON = u'''{
    "errcode":9,
    "info":"invalid json data"
    }'''
    
UERE_LOGOUT = u'''{
    "errcode":10,
    "info":"invalid json data"
    }'''

UER_NOLOGIN = u'''{
    "errcode":11,
    "info":"user has not loged in"
    }'''