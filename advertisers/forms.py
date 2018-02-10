from django import forms
from django.forms import inlineformset_factory

from . import models


class AdvertiserForm(forms.ModelForm):
    class Meta:
        model = models.Advertiser
        fields = ['name', 'email', ]


AddressFormSet = inlineformset_factory(models.Advertiser, models.Address,
                                       fields=['street', 'zip_code', 'county',
                                               'city', 'country'],
                                       extra=0)
BillingAddressFormSet = inlineformset_factory(models.Advertiser,
                                              models.BillingAddress,
                                              fields=['title', 'street',
                                                      'zip_code', 'email',
                                                      'tax_office',
                                                      'tax_number', 'county',
                                                      'city', 'country'],
                                              extra=0)
