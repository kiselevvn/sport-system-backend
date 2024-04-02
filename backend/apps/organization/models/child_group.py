from django.db import models
from django.utils.translation import gettext as _


class ChildGroup(models.Model):
    """
    Образоватеьная Подгруппа
    """

    сhar_code = models.CharField(
        _("Символьный код"), max_length=6, blank=True, null=True
    )
    order = models.PositiveIntegerField(
        verbose_name=_("Фактический порядковый номер"), default=0
    )

    users = models.ManyToManyField(
        "users.User",
    )
    education_group = models.ForeignKey(
        "organization.EducationGroup",
        verbose_name=_("Группа"),
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    @property
    def name(self):
        """
        Наименование подгруппы
        """
        return self.сhar_code if self.сhar_code else str(self.order)

    class Meta:
        verbose_name = _("Группа")
        verbose_name_plural = _("Подгруппы")
