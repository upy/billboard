from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


class Representative(User):
    """
    The Representative class defines the main storage point for the advertiser
    representative.

    """
    phone = models.CharField(
        _("Phone"), max_length=30, help_text=_("ex: +901234567890")
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        default_permissions = ("add", "change", "delete", "view")
        db_table = "representative"
        verbose_name = _("Representative")
        verbose_name_plural = _("Representatives")
