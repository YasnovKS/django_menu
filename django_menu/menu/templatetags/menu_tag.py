from menu.models import MenuItem
from django import template

register = template.Library()


@register.inclusion_tag('menu.html', takes_context=True)
def show_menu(context):
    obj = context.get('obj')
    menu = MenuItem.objects.all()
    return {'menu': menu,
            'obj': obj,
            }
