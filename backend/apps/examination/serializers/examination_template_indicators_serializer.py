from rest_framework.serializers import ModelSerializer

from backend.apps.examination.models import ExaminationTemplateIndicators

from .groups_indicators_serializer import GroupIndicatorsSerializer
from .indicator_serializer import IndicatorSerializer


class ExaminationTemplateIndicatorsSerializer(ModelSerializer):
    """
    Показатели шаблонов обследований
    """

    indicator = IndicatorSerializer()
    group_indicator = GroupIndicatorsSerializer()

    class Meta:
        model = ExaminationTemplateIndicators
        # fields = [
        #     "id",
        #     "indicator",
        #     "group_indicator",
        # ]
        fields = "__all__"
