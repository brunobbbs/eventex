from django.contrib import admin
from django.utils.timezone import now

from eventex.subscriptions.models import Subscription


class SubscriptionModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'cpf', 'phone', 'email', 'created_at', 'subscribed_today', 'paid')
    search_fields = ('name', 'cpf', 'phone', 'email', 'created_at')
    list_filter = ('created_at', 'paid')
    date_hierarchy = 'created_at'

    actions = ['mark_as_paid']

    def subscribed_today(self, obj):
        return obj.created_at.date() == now().date()

    subscribed_today.short_description = 'Inscrito hoje?'
    subscribed_today.boolean = True

    def mark_as_paid(self, request, queryset):
        pass


admin.site.register(Subscription, SubscriptionModelAdmin)
