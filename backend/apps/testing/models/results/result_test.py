from django.db import models
from django.utils.translation import gettext as _


class ResultTest(models.Model):
    """
    Результат тестирования
    """

    test_template = models.ForeignKey(
        "testing.TestTemplate",
        verbose_name=_("Тест"),
        on_delete=models.CASCADE,
        related_name="results_tests",
    )
    user = models.ForeignKey(
        "users.User",
        verbose_name=_("Пользователь"),
        on_delete=models.CASCADE,
        related_name="result_tests",
    )
    result_score = models.PositiveIntegerField(
        _("Кол-во баллов"), blank=True, null=True
    )
    date = models.DateField(_("Дата проведения"), blank=True, null=True)
    date_created = models.DateTimeField(
        auto_now_add=True, verbose_name=_("Дата создания")
    )

    @property
    def name(self):
        return f"{self.user} - {self.test}"

    class Meta:
        verbose_name = _("Результат тестирования")
        verbose_name_plural = _("Результаты тестирования")
        unique_together = ["test_template", "date", "user"]
