"""
WSGI config for stackoverflow_api project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os
import sys 

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "stackoverflow_api.settings")

# Add the detection directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'detection', 'api_client'))


application = get_wsgi_application()
