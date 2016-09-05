#coding=utf-8
from django.http import HttpResponse
from django.conf import settings

def app_context_proc(request):
    
    domain = settings.DOMAIN_NAME;
    store = settings.STORE_DOMAIN;
    return {'menu':domain + '/app/',
            'menu1':domain + '/neoforum/',
            'menu1_title':'forum',
            'menu1_1':domain +'/neoforum/forum/',
            'menu1_title_1':'topic',
            'menu1_2':domain +'/neoforum/user/',
            'menu1_title_2':'user panel',
            'menu2':domain +'/weblog/',
            'menu2_title':'blog',
            'menu3':store + '/store/',
            'menu3_title':'store',
            'menu3_1':store +'/store/',
            'menu3_title_1':'product',
            'menu3_2':store +'/store/',
            'menu3_title_2':'shipping',
            'menu3_3':store +'/store/',
            'menu3_title_3':'payment',
            'menu3_4':store +'/store/',
            'menu3_title_4':'tax',
            'menu3_5':store +'/store/',
            'menu3_title_5':'ext',            
            };
    '''return {'menu':'http://weixinofneo.sinaapp.com/app/',
            'menu1':'http://weixinofneo.sinaapp.com/neoforum/',
            'menu1_title':'forum',
            'menu1_1':'http://weixinofneo.sinaapp.com/neoforum/forum/',
            'menu1_title_1':'topic',
            'menu1_2':'http://weixinofneo.sinaapp.com/neoforum/user/',
            'menu1_title_2':'user panel',
            'menu2':'http://weixinofneo.sinaapp.com/weblog/',
            'menu2_title':'blog',
            'menu3':'http://neoweixin.sinaapp.com/store/',
            'menu3_title':'store',
            'menu3_1':'http://neoweixin.sinaapp.com/store/',
            'menu3_title_1':'product',
            'menu3_2':'http://neoweixin.sinaapp.com/store/',
            'menu3_title_2':'shipping',
            'menu3_3':'http://neoweixin.sinaapp.com/store/',
            'menu3_title_3':'payment',
            'menu3_4':'http://neoweixin.sinaapp.com/store/',
            'menu3_title_4':'tax',
            'menu3_5':'http://neoweixin.sinaapp.com/store/',
            'menu3_title_5':'ext',            
            };'''