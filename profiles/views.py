from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.utils.translation import ugettext_lazy as _
from django.views.generic import UpdateView

from . import models

decorators = [login_required, ]


@method_decorator(decorators, name='dispatch')
class LoggedInRepresentativeUpdateView(SuccessMessageMixin, UpdateView):
    """
    The view class for editing the loggedIn representative details. It will
    have authorized to edit only self-details.
    """
    success_message = _('Your profile details was changed.')
    model = models.Representative
    fields = ['username', 'first_name', 'last_name', 'email', 'phone']
    template_name = 'profiles/profile_update_form.html'
    success_url = reverse_lazy('profile')

    def get_object(self, queryset=None):
        """
        Return the current loggedIn representative instance.
        """
        return self.request.user.representative
