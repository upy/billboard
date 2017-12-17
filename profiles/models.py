from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Representative(models.Model):
    """
    The Representative class defines the main storage point for the customer
    representative.

    """
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    phone = models.CharField(_('Phone'), max_length=30,
                             help_text=_('ex: +901234567890'))

    class Meta:
        db_table = 'representative'
        verbose_name = _('Representative')
        verbose_name_plural = _('Representatives')
