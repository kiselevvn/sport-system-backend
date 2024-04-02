from django.db import models
from django.utils.translation import gettext as _


class ExaminationTemplate(models.Model):
    """
    Medical Examination Template
    Шаблон медицинского обследования

    """

    name = models.CharField(
        verbose_name=_("Наименование"), max_length=125, blank=True, null=True
    )
    description = models.TextField(
        verbose_name=_("Описание"), blank=True, null=True
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
