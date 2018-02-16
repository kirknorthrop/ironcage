from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from tickets.models import Order, Ticket

from import_export.admin import ExportMixin

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin, ExportMixin):
    pass


def make_published(modeladmin, request, queryset):
    print(queryset)

make_published.short_description = "Mark selected stories as published"

@admin.register(Ticket)
class TicketAdmin(ExportMixin, admin.ModelAdmin):

    view_on_site = False
    fields = readonly_fields = ('ticket_id', 'order', 'thu', 'fri', 'sat', 'sun', 'mon')
    list_display = fields + ('link_to_owner',)
    list_filter = ('thu', 'fri', 'sat', 'sun', 'mon')
    search_fields = ['owner__name']
    actions = [make_published]

    def link_to_owner(self, obj):
        url = reverse('admin:accounts_user_change', args=[obj.owner.id])
        return format_html("<a href='{}'>{}</a>", url, obj.owner.name)
    link_to_owner.admin_order_field = 'owner'
    link_to_owner.short_description = 'owner'
