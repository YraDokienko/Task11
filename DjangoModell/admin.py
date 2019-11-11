from django.contrib import admin
from .models import TypeGroupModel


class TypeGroupModelAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'char', 'bigInteger', 'binary', 'decimal', 'float', 'integer', 'positiveInteger',
        'positiveSmallInteger', 'smallInteger', 'text', 'file', 'date',
        'dateTime', 'duration', 'time', 'boolean', 'nullBoolean', 'email', 'genericIPAddress',
        'Slug', 'URL', 'UUID', 'FilePath', 'Image',
    ]
    list_display_links = ['char', ]
    list_editable = ['bigInteger', 'integer', 'decimal', ]
    list_filter = ['decimal', 'float', 'integer', ]
    search_fields = ['char']
    ordering = ['char']


admin.site.register(TypeGroupModel, TypeGroupModelAdmin)
