from django.contrib import admin

from pis_ledger.models import Ledger
from pis_ledger.models import PaymentLedger


class LedgerAdmin(admin.ModelAdmin):
    list_display = (
        '__unicode__', 'retailer', 'amount', 'description', 'created_at'
    )
    search_fields = (
        'customer__customer_name', 'customer__customer_phone',
        'customer__retailer__name'
    )
    raw_id_fields = ('customer',)

    @staticmethod
    def retailer(obj):
        return obj.retailer.name


class PaymentLedgerAdmin(admin.ModelAdmin):
    list_display = (
        '__unicode__', 'retailer', 'amount', 'created_at'
    )
    search_fields = (
        'customer__customer_name', 'customer__customer_phone',
        'customer__retailer__name'
    )
    raw_id_fields = ('customer',)

    @staticmethod
    def retailer(obj):
        return obj.retailer.name


admin.site.register(Ledger, LedgerAdmin)
admin.site.register(PaymentLedger, PaymentLedgerAdmin)