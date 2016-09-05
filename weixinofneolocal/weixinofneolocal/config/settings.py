# Django settings for weixinofneo project.
# coding=utf-8
import os
import sys 

def AddAppPath():
    sys.path.append(os.path.join(os.path.dirname(__file__), '../').replace('\\', '/'))

AddAppPath()

ROOT_PATH = os.path.join(os.path.dirname(__file__), '../').replace('\\', '/')
LOG_PATH = os.path.join(os.path.dirname(__file__), '../logs/').replace('\\', '/')
APP_STATIC = os.path.join(ROOT_PATH, 'app/static/').replace('\\', '/')

# add moudule path
sys.path.append(ROOT_PATH + 'libs/')
#sys.path.append(ROOT_PATH + 'libs/PIL/')
#sys.path.append(ROOT_PATH + 'libs/pytz/')
sys.path.append(ROOT_PATH + 'libs/pygments/')
sys.path.append(ROOT_PATH + 'libs/djangocaptcha/')

# ENV = 'SAE'
ENV = 'VM'

if ENV == "SAE":
    DEBUG = False
else:
    DEBUG = True
    
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('neo', 'guojing_neo@163.com'),
)

MANAGERS = ADMINS

if ENV == "SAE":
    import sae.const
    '''DOMAIN = ''
    MYSQL_HOST = 'localhost'
    MYSQL_PORT = '3306'
    MYSQL_USER = 'root'
    MYSQL_PASS = 'root'
    MYSQL_DB   = 'app_pylabs'''
    DATABASES = {
        'default': {
        'ENGINE': 'django.db.backends.mysql',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': sae.const.MYSQL_DB,  # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': sae.const.MYSQL_USER,
        'PASSWORD': sae.const.MYSQL_PASS,
        'HOST': sae.const.MYSQL_HOST,  # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': sae.const.MYSQL_PORT,  # Set to empty string for default.
        }
    }
elif ENV == "VM":
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': 'mysite',  # Or path to database file if using sqlite3.
            # The following settings are not used with sqlite3:
            'USER': 'root',
            'PASSWORD': '805118680',
            'HOST': '10.105.101.58',  # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
            'PORT': '',  # Set to empty string for default.
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': 'db.db',  # Or path to database file if using sqlite3.
            # The following settings are not used with sqlite3:
            'USER': '',
            'PASSWORD': '',
            'HOST': '',  # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
            'PORT': '',  # Set to empty string for default.
        }
    }

if ENV == "VM":
    DOMAIN_NAME = 'site1'
    STORE_DOMAIN = ''
    SITE_ID = 1
elif ENV == "SAE":
    DOMAIN_NAME = ''
    STORE_DOMAIN = ''
    SITE_ID = 2

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Asia/Shanghai'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'zh-cn'


# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = False

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
if ENV == "VM":
    MEDIA_ROOT = os.path.join(os.path.dirname(__file__), '../media/').replace('\\', '/')
    MEDIA_URL = '/media/'
    STATIC_ROOT = os.path.join(os.path.dirname(__file__), '../static/').replace('\\', '/')
    STATIC_URL = '/site1/static/'
else:
    MEDIA_ROOT = 'http://weixinofneo-media.stor.sinaapp.com/'
    MEDIA_URL = None
    STATIC_ROOT = os.path.join(os.path.dirname(__file__), '../static/').replace('\\', '/')
    STATIC_URL = '/static/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
#STATIC_ROOT = os.path.join(os.path.dirname(__file__), '../static/').replace('\\', '/')

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
#STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    # os.path.join(os.path.dirname(__file__),'../utils/ueditor/').replace('\\','/'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'w-7fr8l+x)g^c1&7i(&(!hz4uktmg@zk$n_ark3%g=y^jleuc5'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'app_namespace.Loader',
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
    
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    # warning
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # forum
    'forumapp.diamandas.userpanel.userMiddleware.userMiddleware',
    # blog
    # satchmo
    # "threaded_multihost.middleware.ThreadLocalMiddleware",
    # "satchmo_store.shop.SSLMiddleware.SSLRedirect",
)

if ENV=='SAE':
    ROOT_URLCONF = 'config.urls'
elif ENV=='VM':
    ROOT_URLCONF = 'config.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'config.wsgi.application'


TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(os.path.dirname(__file__), '../templates/'),
    os.path.join(os.path.dirname(__file__), '../templates/debug/'),
    os.path.join(os.path.dirname(__file__), '../templates/admin/interface/'),
    os.path.join(os.path.dirname(__file__), '../utils/ueditor/static/ueditor/'),
    os.path.join(os.path.dirname(__file__), '../utils/ueditor13/static/ueditor13/'),
    # forumapp
    os.path.join(os.path.dirname(__file__), '../forumapp/diamandas/myghtyboard/templates/'),
    os.path.join(os.path.dirname(__file__), '../forumapp/diamandas/myghtyboard/templates/myghtyboard/'),
    os.path.join(os.path.dirname(__file__), '../forumapp/diamandas/userpanel/templates/'),
    # os.path.join(os.path.dirname(__file__),'../forumapp/diamandas/userpanel/templates/userpanel/'),
    # satchmo
    # os.path.join(os.path.dirname(__file__),'../satchmo/'),
    # renovation
    os.path.join(os.path.dirname(__file__), '../renovation/templates/'),
    # zinnia
    os.path.join(os.path.dirname(__file__), '../zinnia/templates/'),
    #android
    os.path.join(os.path.dirname(__file__),'../android/templates/'),
)   

# AUTH_USER_MODEL = "userpanel.Profile"
# forumapp
# Domain URL used for creating full links in forum admin emails
SITE_DOMAIN = 'http://weixinofneo.sinaapp.com/neoforum/' 

NOTIFY_ADMINS = False  # if true add topic/post will send a email to admin
FORUM_MAX_ANONYMOUS_POSTS_PER_HOUR = 10  # how many posts may be made by anonymous within an hour from now
FORUM_MAX_USER_POST_PER_HOUR = 10  # how many posts may be made by every logged in user within an hour from now. 0 - no limit
FORUM_USE_RECAPTCHA = True  # if true will show recaptha for users with < 5 posts


LOGIN_URL = '/neoforum/user/login/'
#LOGIN_URL = '/renovation/login/'
LOGIN_REDIRECT_URL = '/neoforum/user/'
#AUTH_PROFILE_MODULE = 'userpanel.Profile'
AUTH_PROFILE_MODULE = 'app.UserProfile'

# blog

TEMPLATE_CONTEXT_PROCESSORS = (
  'django.contrib.auth.context_processors.auth',
  'django.core.context_processors.i18n',
  'django.core.context_processors.request',
  'django.core.context_processors.media',
  'django.core.context_processors.static',
  'django.core.context_processors.debug',
  'django.contrib.messages.context_processors.messages',
  'django.core.context_processors.csrf',  # warning
  # app
  'app.context_processors.app_context_proc',
  # blog
  'zinnia.context_processors.version',  # Optional
  # satchmo
  # 'satchmo.satchmo_store.shop.context_processors.settings',
)
"""Settings of Zinnia"""
# from zinnia.xmlrpc import ZINNIA_XMLRPC_METHODS
# XMLRPC_METHODS = ZINNIA_XMLRPC_METHODS
# from zinnia.settings import *
ZINNIA_MARKUP_LANGUAGE = 'MarkDown'
# satchmo
"""Settings of renovation"""
# renovation
'''AUTHENTICATION_BACKENDS = (  
  
    'renovation.backends.DisignerBackend',  
    'renovation.backends.WorkerBackend',  
    'renovation.backends.Companybackend',  
    'django.contrib.auth.backends.ModelBackend'
) '''

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_admin_bootstrapped.bootstrap3',
    'django_admin_bootstrapped',
    'zinnia_bootstrap',
    # common tools
    # weixin
    'app',
    'interface',
    # blog app,
    'utils.ueditor',
    'utils.ueditor13',
    'utils.bs4',
    'utils.mptt',
    'utils.tagging',
    'utils.xmlrpc',
    'utils.markdown',
    'django_comments', 
    'zinnia',
    # forum app
    'forumapp.diamandas.recaptchawidget',
    'forumapp.diamandas.myghtyboard',
    'forumapp.diamandas.userpanel',
    # satchmo
    # renovation
    # 'renovation',
    
    'django.contrib.sitemaps',
    # Uncomment the next line to enable the admin:s
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs'
    # 'utils.south',
    # 'south',
    'android',
   
)
#
import django
if django.VERSION < (1, 5)  or  ENV=="VM":
    SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'
else:
    SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
           
}
