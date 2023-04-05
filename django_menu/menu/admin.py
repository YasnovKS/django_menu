from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from menu.models import MenuItem


admin.site.register(MenuItem, DraggableMPTTAdmin)
