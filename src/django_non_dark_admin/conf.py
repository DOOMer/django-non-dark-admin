from django.conf import settings
from django.contrib.auth import get_user_model


def disable_dark_mode(user=None):
    user_model = get_user_model()
    has_user_preference = hasattr(user_model, "disable_dark_mode")

    DISABLE_DARK_MODE = (
        getattr(user, "disable_dark_mode", False)
        if has_user_preference and user
        else getattr(settings, "DISABLE_DARK_MODE", False)
    )
    return int(DISABLE_DARK_MODE)
