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

    class Meta:
        verbose_name = _("Событие")
        verbose_name_plural = _("События")
