from django.db import models
from django.utils.translation import gettext as _

from backend.apps.services.models import (
    DateCreatedMixin,
    DescriptionMixin,
    NameMixin,
)


class Event(NameMixin, DescriptionMixin, DateCreatedMixin):
    """
    Event
    Событие
    """

    date_start = models.DateTimeField(verbose_name=_("Дата начала события"), blank=True, null=True)
    date_end = models.DateTimeField(verbose_name=_("Дата начала события"), blank=True, null=True)

    class Meta:
        verbose_name = _("Событие")
        verbose_name_plural = _("События")
