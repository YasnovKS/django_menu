from django.shortcuts import render
from menu.models import MenuItem


def index(request):
    return render(request, 'base.html')


def detail_page(request, item_id):
    template = 'detail.html'
    children_items = MenuItem.objects.get(id=item_id).get_children()
    return render(request, template, {'context': children_items})
