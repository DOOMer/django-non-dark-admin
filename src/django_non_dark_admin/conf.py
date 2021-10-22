
from django.conf import settings

DISABLE_DARK_MODE = int(getattr(settings, 'DISABLE_DARK_MODE', False))