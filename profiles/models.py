from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)

    class Meta:
        db_table = 'profile'
        verbose_name = _('Profile')
        verbose_name_plural = _('Profiles')
