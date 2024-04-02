from django.db import models
from django.utils.translation import gettext as _


class ResultQuestion(models.Model):
    """
    Вопрос результатов тестирования
    """

    result_test = models.ForeignKey(
        "testing.ResultTest",
        verbose_name=_("Результат тестирования"),
        on_delete=models.CASCADE,
        related_name="questions",
    )

    question = models.ForeignKey(
        "testing.Question",
        verbose_name=_("Вопрос"),
        on_delete=models.CASCADE,
    )
    date_created = models.DateTimeField(
        auto_now_add=True, verbose_name=_("Дата создания")
    )

    def __str__(self):
        return f"{self.question.text}"

    class Meta:
        verbose_name = _("Ответы на вопрос")
        verbose_name_plural = _("Ответы на вопрос")
        unique_together = ["result_test", "question"]
