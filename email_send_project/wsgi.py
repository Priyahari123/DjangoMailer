"""
WSGI config for email_send_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os
import sys

path = '/home/Haripriya/DjangoMailer'
if path not in sys.path:
    sys.path.insert(0, path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'email_send_project.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

