# coding=utf-8
import os
import sys
import django.core.handlers.wsgi

# sys.path.append(os.path.join(os.path.dirname(__file__), 'config'))
# sys.path.append('/usr/local/lib/python2.7/dist-packages/Django-1.7.1-py2.7.egg/django')
#sys.path.append('/home/neo/workspace/weixinofneolocal/weixinofneolocal')
sys.path.append(os.path.dirname(__file__))
sys.path.append(os.path.join(os.path.dirname(__file__), 'config'))
os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
# application = django.core.handlers.wsgi.WSGIHandler()
