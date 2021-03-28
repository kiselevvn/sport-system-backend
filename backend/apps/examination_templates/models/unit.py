from django.utils.translation import gettext as _
from backend.apps.services.models import (
    NameMixin,
    ShortNameMixin,
    DescriptionMixin,
)


class Unit(NameMixin, ShortNameMixin, DescriptionMixin):
    """
    Unit
    Единица измерения
    """

    class Meta:
        verbose_name = _("Unit")
        verbose_name_plural = _("Unit's")
