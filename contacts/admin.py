from django.contrib import admin

from contacts.models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('code', 'first_name', 'last_name', 'email', 'create_datetime')
    search_fields = ('code', 'first_name', 'email')
    list_per_page = 20
    list_max_show_all = 1000
    ordering = ('-create_datetime',)
    list_editable = ('first_name', 'last_name')
