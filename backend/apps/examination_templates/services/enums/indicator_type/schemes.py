from django.utils.translation import gettext as _
from .schemes_source import (
    IntegerIndiactorSchema,
    FloatIndiactorSchema,
)

INDIACTOR_SCHEMES = {
    1: {
        "schema": IntegerIndiactorSchema,
        "name": _("Integer"),
    },
    2: {
        "schema": FloatIndiactorSchema,
        "name": _("float"),
    },
}
