
from django import template
from ..conf import DISABLE_DARK_MODE

register = template.Library()


@register.inclusion_tag("django_non_dark_admin/darkmode_switch.html", takes_context=True)
def admin_darkmode_switch(context):

    context['disable_admin_dark'] = DISABLE_DARK_MODE

    return context