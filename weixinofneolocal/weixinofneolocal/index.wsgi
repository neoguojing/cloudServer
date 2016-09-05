import sys
import os.path
  
os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings'
sys.path.append(os.path.join(os.path.dirname(__file__), 'config'))

import sae
from config import wsgi

application = sae.create_wsgi_app(wsgi.application)

