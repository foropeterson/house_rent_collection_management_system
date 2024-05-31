# properties/admin.py

from django.contrib import admin
from .models import Property, News

class PropertyAdmin(admin.ModelAdmin):
    list_display = ('title', 'address', 'rent', 'available')
    search_fields = ('title', 'address')
    list_filter = ('available',)

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title',)
    list_filter = ('created_at',)

admin.site.register(Property, PropertyAdmin)
admin.site.register(News, NewsAdmin)
