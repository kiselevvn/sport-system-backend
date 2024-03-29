from django.db import models
from django.utils.translation import gettext as _

from backend.apps.services.models import DescriptionMixin, NameMixin

from .group_indicators import GroupIndicators


class ExaminationTemplate(NameMixin, DescriptionMixin):
    """
    Medical Examination Template
    Шаблон медицинского обследования

    groups_indicators - группа показателей медецинского обследования
    сгрупированных по общему признаку
    """

    groups_indicators = models.ManyToManyField(
        GroupIndicators, verbose_name=_("Группа показателей")
    )

    scheme = models.JSONField(
        _("Схема ограничений ввода"), blank=True, null=True
    )

    is_publish = models.BooleanField(
        verbose_name=_("Является опубликованным"),
        default=False,
    )

    class Meta:
        verbose_name = _("Шаблон медицинского обследования")
        verbose_name_plural = _("Шаблоны медицинских обследований")
