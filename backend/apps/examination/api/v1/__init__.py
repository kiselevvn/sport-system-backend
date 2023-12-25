from .examination_template_indicators_views import (
    ExaminationTemplateIndicatorsViewSet,
)
from .examination_template_views import ExaminationTemplateViewSet
from .examination_views import ExaminationViewSet
from .groups_indicators_views import GroupIndicatorsViewSet
from .indicator_views import IndicatorViewSet

__all__ = [
    "ExaminationViewSet",
    "ExaminationTemplateViewSet",
    "IndicatorViewSet",
    "GroupIndicatorsViewSet",
    "ExaminationTemplateIndicatorsViewSet",
]
