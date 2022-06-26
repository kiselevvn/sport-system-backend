from django.db import models
from django.utils.translation import gettext as _

from backend.apps.services.models import DateCreatedMixin, OrderMixin


class ChildGroup(DateCreatedMixin, OrderMixin):
    """
    Подгруппа
    """

    сhar_code = models.CharField(_("Символьный код"), max_length=6, blank=True, null=True)

    @property
    def name(self):
        """
        Наименование подгруппы
        """
        return self.сhar_code if self.сhar_code else str(self.order)

    class Meta:
        verbose_name = _("Группа")
        verbose_name_plural = _("Подгруппы")
