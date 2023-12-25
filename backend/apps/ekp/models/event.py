from django.db import models
from django.utils.translation import gettext as _


class Event(models.Model):
    """
    Событие
    """

    name = models.CharField(
        verbose_name=_("Наименование"), max_length=125, blank=True, null=True
    )
    slug = models.SlugField(_("Прямая ссылка"), blank=True, null=True)
    date_start = models.DateTimeField(
        verbose_name=_("Дата начала события"), blank=True, null=True
    )
    date_end = models.DateTimeField(
        verbose_name=_("Дата окончания события"), blank=True, null=True
    )

    class Meta:
        verbose_name = _("Событие")
        verbose_name_plural = _("События")
