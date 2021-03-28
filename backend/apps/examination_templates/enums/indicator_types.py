from django.db import models
from django.utils.translation import gettext as _


class TypeIndiactor(models.IntegerChoices):
    INTEGER = 1, _("Integer")
    FLOAT = 2, _("Float")
    # LIST = 3, _("Junior")
    # SENIOR = 4, _("Senior")
    # GRADUATE = 5, _("Graduate")
