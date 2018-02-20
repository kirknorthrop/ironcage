from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from tickets.models import Order, Ticket
from tickets.actions import refund_order

from import_export.admin import ExportMixin
from django_object_actions import DjangoObjectActions


class OurActionsOnlyMixin():

    def has_add_permission(self, request):
        return False


    def has_delete_permission(self, request, obj=None):
        return False

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions


@admin.register(Order)
class OrderAdmin(DjangoObjectActions, OurActionsOnlyMixin, admin.ModelAdmin):

    def refund(self, request, obj):
        refund_order(obj)


    def get_change_actions(self, request, object_id, form_url):
        actions = super().get_change_actions(request, object_id, form_url)
        actions = list(actions)

        obj = self.model.objects.get(pk=object_id)
        if obj.status == 'successful':
            actions.append('refund')

        return actions

    view_on_site = False
    fields = ('link_to_purchaser', 'rate', 'status', 'stripe_charge_id', 'stripe_charge_created',
              'stripe_charge_failure_reason', 'company_name', 'company_addr')
    readonly_fields = ('link_to_purchaser', 'rate', 'status', 'stripe_charge_id',
                       'stripe_charge_created', 'stripe_charge_failure_reason')
    list_display = ('order_id', 'link_to_purchaser', 'rate', 'status')
    list_filter = ('rate', 'status')
    search_fields = ['purchaser__name']

    def link_to_purchaser(self, obj):
        url = reverse('admin:accounts_user_change', args=[obj.purchaser.id])
        return format_html("<a href='{}'>{}</a>", url, obj.purchaser.name)
    link_to_purchaser.admin_order_field = 'purchaser'
    link_to_purchaser.short_description = 'purchaser'


@admin.register(Ticket)
class TicketAdmin(DjangoObjectActions, OurActionsOnlyMixin, admin.ModelAdmin):

    def refund(self, request, obj):
        refund_order(obj.order)

    change_actions = ['refund']

    view_on_site = False
    fields = readonly_fields = ('ticket_id', 'link_to_owner', 'link_to_order', 'thu', 'fri', 'sat', 'sun', 'mon')
    list_display = ('ticket_id', 'link_to_owner', 'link_to_order', 'thu', 'fri', 'sat', 'sun', 'mon')
    list_filter = ('thu', 'fri', 'sat', 'sun', 'mon')
    search_fields = ['owner__name']

    def link_to_owner(self, obj):
        url = reverse('admin:accounts_user_change', args=[obj.owner.id])
        return format_html("<a href='{}'>{}</a>", url, obj.owner.name)
    link_to_owner.admin_order_field = 'owner'
    link_to_owner.short_description = 'owner'

    def link_to_order(self, obj):
        url = reverse('admin:tickets_order_change', args=[obj.order.id])
        return format_html("<a href='{}'>{}</a>", url, obj.order.order_id)
    link_to_order.admin_order_field = 'order'
