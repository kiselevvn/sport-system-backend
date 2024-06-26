from django.db import models
from django.utils.translation import gettext as _

from backend.apps.services.models import (
    DescriptionMixin,
    NameMixin,
)


class TestTemplate(NameMixin, DescriptionMixin):
    """
    Шаблон тестирования
    """

    slug = models.SlugField(_("Постоянная ссылка"))
    is_open = models.BooleanField(_("Является открытым"), default=False)
    is_published = models.BooleanField(
        _("Является опубликованным"), default=False
    )
    max_win_score = models.IntegerField(
        _("Максимальный балл"), blank=True, null=True
    )

    def __str__(self):
        if self.name and self.name != "":
            return self.name
        return self.slug

    class Meta:
        verbose_name = _("Шаблон тестирования")
        verbose_name_plural = _("Шаблоны тестирований")
