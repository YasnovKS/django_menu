from django.contrib import admin
from menu.models import Menu, MenuItem
from mptt.admin import DraggableMPTTAdmin


admin.site.register(Menu, admin.ModelAdmin)
admin.site.register(MenuItem, DraggableMPTTAdmin,
                    list_display=('tree_actions',
                                  'indented_title',
                                  'main_menu'
                                  )
                    )
