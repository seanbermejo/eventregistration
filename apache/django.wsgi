import os
import sys

path = '/home/sean/projects'
project = '/home/sean/projects/eventregistration'
env = '/home/sean/env/lib/python2.7/site-packages'

if path not in sys.path:
    sys.path.append(path)

if project not in sys.path:
    sys.path.append(project)

if env not in sys.path:
    sys.path.append(env)

sys.stdout = sys.stderr

os.environ['DJANGO_SETTINGS_MODULE'] = 'eventregistration.settings'


import django.core.handlers.wsgi

_application = django.core.handlers.wsgi.WSGIHandler()

def application(environ, start_response):
    environ['PATH_INFO'] = environ['SCRIPT_NAME'] + environ['PATH_INFO']
    return _application(environ, start_response)

