from django.db import models
from django.utils.translation import gettext_lazy as _


class Advertiser(models.Model):
    """The Advertiser class defines the main storage point for advertiser."""
    name = models.CharField(_('Name'), max_length=255,
                            help_text=_('Company name'))
    email = models.EmailField(_('E-mail'), help_text=_('E-mail address'))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        default_permissions = ('add', 'change', 'delete', 'view')
        db_table = 'advertiser'
        verbose_name = _('Advertiser')
        verbose_name_plural = _('Advertisers')


class Address(models.Model):
    """The Address class defines the main storage point for postal address."""
    advertiser = models.OneToOneField(Advertiser, on_delete=models.CASCADE,
                                      verbose_name=_('Advertiser'))
    street = models.TextField(_('Address'))
    zip_code = models.CharField(_('Zip code'), max_length=20)
    county = models.CharField(_('County'), max_length=100)
    city = models.CharField(_('City'), max_length=100)
    country = models.CharField(_('Country'), max_length=100)

    class Meta:
        default_permissions = ('add', 'change', 'delete', 'view')
        db_table = 'address'
        verbose_name = _('Address')
        verbose_name_plural = _('Addresses')


class BillingAddress(models.Model):
    """
    The BillingAddress class defines the main storage point for billing
    address.
    """
    advertiser = models.OneToOneField(Advertiser, on_delete=models.CASCADE,
                                      verbose_name=_('Advertiser'))
    title = models.CharField(_('Title'), max_length=255, blank=True, null=True)
    street = models.TextField(_('Address'))
    zip_code = models.CharField(_('Zip code'), max_length=20)
    email = models.EmailField(_('E-invoice e-mail'), blank=True, null=True)
    tax_office = models.CharField(_('Tax office'), max_length=100)
    tax_number = models.CharField(_('Tax number'), max_length=50)
    county = models.CharField(_('County'), max_length=100)
    city = models.CharField(_('City'), max_length=100)
    country = models.CharField(_('Country'), max_length=100)

    class Meta:
        default_permissions = ('add', 'change', 'delete', 'view')
        db_table = 'billing_address'
        verbose_name = _('Billing address')
        verbose_name_plural = _('Billing addresses')
