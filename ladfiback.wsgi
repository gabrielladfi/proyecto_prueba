import os
from django.core.wsgi import get_wsgi_application

# Establece la variable de entorno DJANGO_SETTINGS_MODULE
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ladfiback.settings")

# Carga la aplicación WSGI
application = get_wsgi_application()
