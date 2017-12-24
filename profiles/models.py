from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Representative(User):
    """
    The Representative class defines the main storage point for the customer
    representative.

    """
    phone = models.CharField(_('Phone'), max_length=30,
                             help_text=_('ex: +901234567890'))

    class Meta:
        db_table = 'representative'
        verbose_name = _('Representative')
        verbose_name_plural = _('Representatives')
