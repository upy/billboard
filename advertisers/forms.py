from django import forms
from django.forms import inlineformset_factory

from . import models


class AdvertiserForm(forms.ModelForm):

    class Meta:
        model = models.Advertiser
        fields = ["name", "email"]


class AddressForm(forms.ModelForm):

    class Meta:
        model = models.Address
        fields = ["street", "zip_code", "county", "city", "country"]


class BillingAddressForm(forms.ModelForm):

    class Meta:
        model = models.BillingAddress
        fields = [
            "title",
            "street",
            "zip_code",
            "email",
            "tax_office",
            "tax_number",
            "county",
            "city",
            "country",
        ]


AddressFormSet = inlineformset_factory(
    models.Advertiser, models.Address, form=AddressForm, extra=1, can_delete=False
)
BillingAddressFormSet = inlineformset_factory(
    models.Advertiser,
    models.BillingAddress,
    form=BillingAddressForm,
    extra=1,
    can_delete=False,
)
