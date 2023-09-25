from rest_framework.serializers import ModelSerializer, JSONField

from backend.apps.examination_templates.models import (
    Indicator,
    GroupIndicators,
    ExaminationTemplate,
)


class IndicatorExaminationTemplateBaseSerializer(ModelSerializer):
    class Meta:
        model = Indicator
        fields = [
            "id",
            "name",
            "description",
            "type_indicator",
            "unit",
        ]


class GroupsIndicatorsExaminationTemplateBaseSerializer(ModelSerializer):

    indicators = IndicatorExaminationTemplateBaseSerializer(
        many=True, read_only=True
    )

    class Meta:
        model = GroupIndicators
        fields = ["id", "name", "description", "indicators"]


class ExaminationTemplateBaseSerializer(ModelSerializer):
    """


    """

    groups_indicators = GroupsIndicatorsExaminationTemplateBaseSerializer(
        many=True, read_only=True
    )

    class Meta:
        model = ExaminationTemplate
        fields = ["id", "name", "description", "groups_indicators"]