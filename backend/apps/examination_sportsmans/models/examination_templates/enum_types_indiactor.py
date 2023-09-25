from django.db import models
from django.utils.translation import gettext as _


class EnumTypesIndiactor(models.IntegerChoices):
    """
    Тип значения атрибута
    """

    INTEGER = 1, _("Integer")
    FLOAT = 2, _("Float")
    # LIST_INTEGER = 3, _("List")
    # LIST_INTEGER = 3, _("List")
