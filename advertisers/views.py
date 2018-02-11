from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.utils.translation import ugettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView

from advertisers import forms
from . import models

decorators = [login_required, ]


@method_decorator(decorators, name='dispatch')
class AdvertiserListView(PermissionRequiredMixin, ListView):
    """The view class for the list of the advertisers."""
    raise_exception = True
    permission_denied_message = _(
        'You do not have permission to see advertisers.')
    permission_required = ('advertisers.view_advertiser',)
    model = models.Advertiser
    template_name = 'advertisers/advertiser_list.html'


@method_decorator(decorators, name='dispatch')
class AdvertiserCreateView(SuccessMessageMixin, PermissionRequiredMixin,
                           CreateView):
    """The view class for creating a new advertiser."""
    raise_exception = True
    permission_denied_message = _(
        'You do not have permission to add advertiser.')
    permission_required = ('advertisers.add_advertiser',)
    form_class = forms.AdvertiserForm
    model = models.Advertiser
    success_message = _('Advertiser details were added.')
    template_name = 'advertisers/advertiser_create_form.html'
    success_url = reverse_lazy('advertiser-list')

    def get(self, request, *args, **kwargs):
        """
        Handle GET requests: instantiate a blank version of the form and
        formsets.
        """
        self.object = None
        return self.render_to_response(self.get_context_data(
            form=self.get_form(),
            address_form_set=forms.AddressFormSet(prefix='address'),
            billing_address_form_set=forms.BillingAddressFormSet(
                prefix='billing_address')))


@method_decorator(decorators, name='dispatch')
class AdvertiserUpdateView(SuccessMessageMixin, PermissionRequiredMixin,
                           UpdateView):
    """The view class for the updating a advertiser details."""
    raise_exception = True
    permission_denied_message = _(
        'You do not have permission to change customer.')
    permission_required = ('advertisers.change_advertiser',)
    model = models.Advertiser
    success_message = _('Customer details were changed.')
    form_class = forms.AdvertiserForm
    template_name = 'advertisers/advertiser_update_form.html'
    success_url = reverse_lazy('advertiser-list')

    def get(self, request, *args, **kwargs):
        """
        Handle GET requests: instantiate a blank version of the form and
        formsets.
        """
        self.object = self.get_object()
        return self.render_to_response(self.get_context_data(
            form=self.get_form(),
            address_form_set=forms.AddressFormSet(prefix='address'),
            billing_address_form_set=forms.BillingAddressFormSet(
                prefix='billing_address')))
