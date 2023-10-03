from rest_framework.serializers import JSONField, ModelSerializer

from backend.apps.examination.models import (
    ExaminationTemplate,
    GroupIndicators,
    Indicator,
)


class IndicatorExaminationTemplateSerializer(ModelSerializer):
    """
    Показатель
    """

    class Meta:
        model = Indicator
        fields = [
            "id",
            "name",
            "description",
            "type_indicator",
            "unit",
        ]


class GroupsIndicatorsExaminationTemplateSerializer(ModelSerializer):
    """
    Группа показателей
    """

    indicators = IndicatorExaminationTemplateSerializer(
        many=True, read_only=True
    )

    class Meta:
        model = GroupIndicators
        fields = ["id", "name", "description", "indicators"]


class ExaminationTemplateSerializer(ModelSerializer):
    """
    Шаблон обследования
    """

    groups_indicators = GroupsIndicatorsExaminationTemplateSerializer(
        many=True, read_only=True
    )

    class Meta:
        model = ExaminationTemplate
        fields = ["id", "name", "description", "groups_indicators"]
