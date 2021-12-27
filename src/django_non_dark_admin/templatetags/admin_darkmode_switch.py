from django import template
from ..conf import disable_dark_mode

register = template.Library()


@register.inclusion_tag(
    "django_non_dark_admin/darkmode_switch.html", takes_context=True
)
def admin_darkmode_switch(context):
    user = getattr(context["request"], "user", None)
    context["disable_admin_dark"] = disable_dark_mode(user)

    return context
