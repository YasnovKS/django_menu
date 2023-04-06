from menu.models import MenuItem
from django import template

register = template.Library()


@register.inclusion_tag('menu.html', takes_context=True)
def draw_menu(context, menu_name):
    obj = context.get('obj')
    menu = MenuItem.objects.filter(main_menu=menu_name)
    return {'menu': menu,
            'obj': obj,
            }
