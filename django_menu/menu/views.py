from django.shortcuts import render, get_object_or_404
from menu.models import MenuItem


def index(request):
    return render(request, 'base.html')


def detail_page(request, item_id):
    template = 'detail.html'
    obj = get_object_or_404(MenuItem, pk=item_id)
    children_items = obj.get_children()
    return render(request, template, {'context': children_items,
                                      'obj': obj
                                      }
                  )
