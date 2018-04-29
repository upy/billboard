"""
WSGI config for billboard project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/dev/howto/deployment/wsgi/
"""

import os  # pragma no coverage

from django.core.wsgi import get_wsgi_application  # pragma no coverage

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "billboard.settings"
)  # pragma no coverage

application = get_wsgi_application()  # pragma no coverage
