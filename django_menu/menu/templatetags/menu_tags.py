from menu.models import MenuItem
from django import template

register = template.Library()


@register.inclusion_tag('menu.html', takes_context=True)
def draw_menu(context, menu_name):
    '''Create menu on any page by tag {% draw_menu "menu_name" %}'''
    obj = context.get('obj')
    menu = MenuItem.objects.filter(main_menu__title=menu_name)
    request = context.get('request')
    page_url = request.get_full_path()
    print(page_url)
    return {'menu': menu,
            'obj': obj,
            'menu_title': menu_name,
            }
