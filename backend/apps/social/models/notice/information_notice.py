from django.db import models
from django.utils.translation import gettext as _
from backend.apps.services.models import (
    DateCreatedMixin,
    DateUpdatedMixin,
)


class InformationNotice(DateCreatedMixin, DateUpdatedMixin):
    """
    model Notice
    модель уведомления
    """

    title = models.CharField(
        verbose_name=_("Заголовок"), max_length=255, blank=True, null=True
    )

    short_body = models.TextField(_("Тело"), blank=True, null=True)

    body = models.TextField(_("Тело"), blank=True, null=True)

    archive_date = models.DateField(
        verbose_name=_("Дата архивации"), default=None, blank=True, null=True
    )
    published_date = models.DateField(
        verbose_name=_("Дата публикации"), default=None, blank=True, null=True
    )
    is_hidden = models.BooleanField(verbose_name=_("Скрыт"), default=True)

    class Meta:
        verbose_name = _("Уведомление")
        verbose_name_plural = _("Уведомления")
        abstract = True
