from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.utils.translation import ugettext_lazy as _
from django.views.generic import CreateView, UpdateView, ListView

from . import models

decorators = [login_required, ]


@method_decorator(decorators, name='dispatch')
class LoggedInRepresentativeUpdateView(SuccessMessageMixin, UpdateView):
    """
    The view class for editing the loggedIn representative details. It will
    have authorized to edit only self-details.
    """
    success_message = _('Your profile was changed.')
    model = models.Representative
    fields = ['username', 'first_name', 'last_name', 'email', 'phone']
    template_name = 'profiles/profile_update_form.html'
    success_url = reverse_lazy('profile')

    def get_object(self, queryset=None):
        """
        Return the current loggedIn representative instance.
        """
        return self.request.user.representative


@method_decorator(decorators, name='dispatch')
class RepresentativeListView(PermissionRequiredMixin, ListView):
    """
    The view class for the list of the representatives.
    """
    raise_exception = True
    permission_denied_message = _(
        'You do not have permission to see representatives.')
    permission_required = ('profiles.view_representative',)
    model = models.Representative
    template_name = 'profiles/representative_list.html'


@method_decorator(decorators, name='dispatch')
class RepresentativeUpdateView(SuccessMessageMixin, PermissionRequiredMixin,
                               UpdateView):
    """
    The view class for the updating a representative details.
    """
    raise_exception = True
    permission_denied_message = _(
        'You do not have permission to change representative.')
    permission_required = ('profiles.change_representative',)
    model = models.Representative
    success_message = _('Representative details were changed.')
    fields = ['username', 'first_name', 'last_name', 'email', 'phone',
              'is_active']
    template_name = 'profiles/representative_update_form.html'
    success_url = reverse_lazy('representative-list')


@method_decorator(decorators, name='dispatch')
class RepresentativeCreateView(SuccessMessageMixin, PermissionRequiredMixin,
                               CreateView):
    """
    The view class for creating a new representative.
    """
    raise_exception = True
    permission_denied_message = _(
        'You do not have permission to add representative.')
    permission_required = ('profiles.add_representative',)
    model = models.Representative
    success_message = _('Representative details were added.')
    fields = ['username', 'first_name', 'last_name', 'email', 'phone',
              'is_active']
    template_name = 'profiles/representative_create_form.html'
    success_url = reverse_lazy('representative-list')
