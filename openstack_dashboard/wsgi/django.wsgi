import logging
import os
import sys
import django.core.handlers.wsgi
from django.conf import settings


# Add the site-packages of the chosen virtualenv to work with
site.addsitedir('/home/geiao/repo/horizon/.venv/lib/python2.7/site-packages')


# Add the app's directory to the PYTHONPATH
sys.path.append('/home/geiao/repo/horizon/openstack_dashboard')



# Add this file path to sys.path in order to import settings
sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(__file__)), '../..'))
os.environ['DJANGO_SETTINGS_MODULE'] = 'openstack_dashboard.settings'
sys.stdout = sys.stderr

DEBUG = False

application = django.core.handlers.wsgi.WSGIHandler()
