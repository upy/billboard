from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AdvertisersConfig(AppConfig):
    name = 'advertisers'
    verbose_name = _('Advertiser')
    verbose_name_plural = _('Advertisers')
