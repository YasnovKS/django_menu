from menu.models import MenuItem
from django import template
from pprint import pprint

register = template.Library()


@register.inclusion_tag('menu.html', takes_context=True)
def show_menu(context):
    request = context.get('request')
    item_id = request.get_full_path().replace('/', '')
    if not item_id:
        menu = MenuItem.objects.all()
        return {'menu': menu}
    selected_node = MenuItem.objects.get(id=item_id)
    menu = selected_node.get_children()
    pprint(menu)
    return {'menu': menu,
            'selected_node': selected_node,
            'item_id': item_id
            }
