from django.utils.translation import gettext as _

from backend.apps.services.models import (
    DescriptionMixin,
    NameMixin,
    ShortNameMixin,
)


class Unit(NameMixin, ShortNameMixin, DescriptionMixin):
    """
    Unit
    Единица измерения
    """

    class Meta:
        verbose_name = _("Единица измерения")
        verbose_name_plural = _("Единицы измерения")
