"""
WSGI config for programme_sous_admin project.

It exposes the WSGI callable as a module-level variable named ``application``.
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'programme_sous_admin.settings')
application = get_wsgi_application()
