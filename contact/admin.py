from django.contrib import admin
from contact.models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'phone', 'email',)
    ordering = ('-id',)
    list_filter = ('created_date',)
    search_fields = ('id', 'first_name', 'last_name',)
    list_per_page = 25
    list_max_show_all = 250
    list_editable = ('phone',)
    list_display_links = ('id', 'first_name',)