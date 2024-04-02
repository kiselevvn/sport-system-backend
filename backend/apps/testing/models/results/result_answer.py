from django.db import models
from django.utils.translation import gettext as _


class ResultAnswer(models.Model):
    """
    Ответ результатов тестирования
    """

    result_question = models.ForeignKey(
        to="testing.ResultQuestion",
        verbose_name=_("Результат тестирования"),
        on_delete=models.CASCADE,
        related_name="answers",
    )

    answers = models.ManyToManyField(
        "testing.Answer", verbose_name=_("Ответы")
    )
    date_created = models.DateTimeField(
        auto_now_add=True, verbose_name=_("Дата создания")
    )

    class Meta:
        verbose_name = _("Ответы на вопрос")
        verbose_name_plural = _("Ответы на вопрос")
