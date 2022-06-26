# flake8: noqa
from .indicator import (
    CreateIndicatorAPIView,
    AllIndicatorsAPIView,
    UpdateIndicatorAPIView,
    RetrieveIndicatorAPIView,
    DestroyIndicatorAPIView,
)

from .unit import (
    CreateUnitAPIView,
    AllUnitsAPIView,
    RetrieveUnitAPIView,
    UpdateUnitAPIView,
    DestroyUnitAPIView,
)


from .examination_template import (
    AllExaminationTemplatesAPIView,
    CreateExaminationTemplateAPIView,
    RetrieveExaminationTemplateAPIView,
)

from .group_indicators import ExaminationTemplateCreateGroupAPIView

__all__ = [
    #
    "AllIndicatorsAPIView",
    "CreateIndicatorAPIView",
    "UpdateIndicatorAPIView",
    "RetrieveIndicatorAPIView",
    "DestroyIndicatorAPIView",
    #
    "CreateUnitAPIView",
    "AllUnitsAPIView",
    "UpdateUnitAPIView",
    "RetrieveUnitAPIView",
    "DestroyUnitAPIView",
    #
    "AllExaminationTemplatesAPIView",
    "CreateExaminationTemplateAPIView",
    "RetrieveExaminationTemplateAPIView",
    #
    "ExaminationTemplateCreateGroupAPIView",
]