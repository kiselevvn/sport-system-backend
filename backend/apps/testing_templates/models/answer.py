from django.db import models
from django.utils.translation import gettext as _

from backend.apps.services.models import DateCreatedMixin


class Answer(DateCreatedMixin):
    """
    Вариант ответа
    """

    question = models.ForeignKey(
        "testing_templates.Question",
        verbose_name=_("Тест"),
        on_delete=models.CASCADE,
        related_name="answers",
    )

    text = models.TextField(_("Текст ответа"), blank=True, null=True)

    number = models.PositiveIntegerField(
        _("Порядковый номер"), blank=True, null=True
    )
    is_win = models.BooleanField(_("Является верным"), default=False)
    score = models.PositiveIntegerField(
        _("Кол-во баллов"), blank=True, null=True
    )

    class Meta:
        verbose_name = _("Вариант ответа")
        verbose_name_plural = _("Варианты ответотв")
