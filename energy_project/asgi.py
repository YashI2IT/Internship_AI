"""
ASGI config for energy_project.
"""

import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'energy_project.settings')

application = get_asgi_application()