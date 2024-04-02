from django.db import models
from django.utils.translation import gettext as _


class Answer(models.Model):
    """
    Вариант ответа
    """

    question = models.ForeignKey(
        to="testing.Question",
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

    def __str__(self):
        return f"{self.text}"

    class Meta:
        verbose_name = _("Вариант ответа")
        verbose_name_plural = _("Варианты ответотв")
