from django.contrib import admin

from . import models


class AddressInline(admin.StackedInline):
    model = models.Address


class BillingAddressInline(admin.StackedInline):
    model = models.BillingAddress


@admin.register(models.Advertiser)
class AdvertiserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    inlines = [AddressInline, BillingAddressInline]
