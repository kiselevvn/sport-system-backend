from django.utils.translation import gettext as _
from backend.apps.examination_templates.schemas import (
    IntegerIndiactorSchema,
    FloatIndiactorSchema,
)

DICT_OF_INDIACTOR_SCHEMES = {
    1: {
        "schema": IntegerIndiactorSchema,
        "name": _("Integer"),
    },
    2: {
        "schema": FloatIndiactorSchema,
        "name": _("float"),
    },
}
