# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import ElementType, Element, Currency, Island, Habitat

class ElementAdmin(admin.ModelAdmin):
    list_display = ('name', 'element_type', 'opposite_element')

class IslandAdmin(admin.ModelAdmin):
    list_display = ('name', 'cost', 'level_available', 'summon_time')

admin.site.register(ElementType)
admin.site.register(Element, ElementAdmin)
admin.site.register(Currency)
admin.site.register(Island)
admin.site.register(Habitat)

# Register your models here.
