from rest_framework.serializers import (
    ModelSerializer,
    JSONField,
    SerializerMethodField,
)
from rest_framework.generics import RetrieveAPIView
from backend.apps.examination_templates.models import (
    ExaminationTemplate,
    Indicator,
    GroupIndicators,
)
from backend.apps.examination_templates.services import get_indicator_scheme


class IndicatorExaminationTemplateSerializer(ModelSerializer):
    # schema = JSONField(
    #     binary=False,
    # )
    schema = SerializerMethodField()

    class Meta:
        model = Indicator
        fields = [
            "id",
            "name",
            "description",
            "type_indicator",
            "unit",
            "schema",
        ]

    def get_schema(self, obj):
        return get_indicator_scheme(obj.type_indicator)


class GroupsIndicatorsExaminationTemplateSerializer(ModelSerializer):

    indicators = IndicatorExaminationTemplateSerializer(
        many=True, read_only=True
    )

    class Meta:
        model = GroupIndicators
        fields = ["id", "name", "description", "indicators"]


class RetrieveExaminationTemplateSerializer(ModelSerializer):

    groups_indicators = GroupsIndicatorsExaminationTemplateSerializer(
        many=True, read_only=True
    )

    class Meta:
        model = ExaminationTemplate
        fields = ["id", "name", "description", "groups_indicators"]


class RetrieveExaminationTemplateAPIView(RetrieveAPIView):
    """
    Retrieve ExaminationTemplate
    """

    serializer_class = RetrieveExaminationTemplateSerializer
    queryset = ExaminationTemplate.objects.all()
