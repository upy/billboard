from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Board(models.Model):
    LEFT = 1
    RIGHT = 2
    BIPARTITE = 3
    STYLES = (
        (LEFT, _('Left side')),
        (RIGHT, _('Right side')),
        (BIPARTITE, _('Bipartite side')),
    )
    MAIN = 1
    INTERMEDIATE = 2
    ARTERIES = (
        (MAIN, _('Main artery')),
        (INTERMEDIATE, _('Intermediate artery')),
    )

    number = models.CharField(_('Number'), max_length=255)
    comment = models.TextField(_('Comment'))
    style = models.PositiveSmallIntegerField(_('Style'), choices=STYLES,
                                             db_index=True)
    latitude = models.DecimalField(_('Latitude'), max_digits=9,
                                   decimal_places=6)
    longitude = models.DecimalField(_('Longitude'), max_digits=9,
                                    decimal_places=6)
    artery = models.PositiveSmallIntegerField(_('Artery type'), db_index=True,
                                              choices=ARTERIES)
    status = models.BooleanField(_('Is active?'), default=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    prepared_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                    verbose_name=_('Prepared by'),
                                    on_delete=models.CASCADE)

    class Meta:
        db_table = 'board'
        verbose_name = _('Board')
        verbose_name_plural = _('Boards')
