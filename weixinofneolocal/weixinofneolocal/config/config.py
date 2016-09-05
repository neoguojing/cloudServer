# coding=utf-8
from django.conf import settings
domain = settings.DOMAIN_NAME
WEIXIN_TOKEN = "neoweixin"
WEIXIN_APPID = "wx41ce13516e1b65ad"
WEIXIN_SECRET = "7c46f29e642d8853afd49e8aa72d8078"
WEIXIN_ID = "gh_baa3b74f106c"
CJYX_APPID = "wxb4a5cc452f6513c0"
CJYX_APPSECRET = "0acfeca212855e5e675cb739d16826c1"
REDIRECT_URL = domain + "/code/"
class Access_Token:
    ACCESS_TOKEN = None
    ACCESS_TOKEN_TIME = 0
    expires_in = 7200
    
class Auth_Token:
    TOKEN = None
    OPENID = None
    REFTOKEN = None
    SCOPE = None
    expires_in = 7200
# TEST

NEO = None
    
# au_token = Auth_Token()
