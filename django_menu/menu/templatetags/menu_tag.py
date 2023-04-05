from menu.models import MenuItem
from django import template
from django.shortcuts import get_object_or_404


register = template.Library()


@register.inclusion_tag('menu.html', takes_context=True)
def show_menu(context):
    menu = MenuItem.objects.all()
    return {'menu': menu}
