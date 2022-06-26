from django.db import models
from django.utils.translation import gettext as _

from backend.apps.services.models import NameMixin

from .question import Question


class MediaObject(NameMixin):
    """
    Медиа объект
    """

    question = models.ForeignKey(
        to=Question,
        verbose_name=_("Тест"),
        on_delete=models.CASCADE,
        related_name="media_objects",
    )

    number = models.PositiveIntegerField(
        _("Порядковый номер"), blank=True, null=True
    )

    url = models.URLField(_("Ссылка"), max_length=200, blank=True, null=True)
    picture = models.ImageField(_("Изображение"), blank=True, null=True)
    html = models.TextField(_("html код"), blank=True, null=True)

    class Meta:
        verbose_name = _("Медиа объект")
        verbose_name_plural = _("Медиа объекты")
