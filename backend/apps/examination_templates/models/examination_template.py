from django.db import models
from django.utils.translation import gettext as _

from backend.apps.services.models import DescriptionMixin, NameMixin


class ExaminationTemplate(NameMixin, DescriptionMixin):
    """
    Medical Examination Template
    Шаблон медицинского обследования
    """

    groups_indicators = models.ManyToManyField(
        "examination_templates.GroupIndicators"
    )

    scheme = models.JSONField(_("Схема"), blank=True, null=True)

    is_publish = models.BooleanField(verbose_name=_("Схема"),default=False,)

    class Meta:
        verbose_name = _("Шаблон медицинского обследования")
        verbose_name_plural = _("Шаблоны медицинских обследований")
