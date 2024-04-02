from rest_framework.serializers import ModelSerializer

from backend.apps.examination.models import ExaminationTemplate

from .examination_template_indicators_serializer import (
    ExaminationTemplateIndicatorsSerializer,
)


class ExaminationTemplateSerializer(ModelSerializer):
    """
    Шаблон обследования
    """

    examination_template_indicators = ExaminationTemplateIndicatorsSerializer(
        many=True
    )

    class Meta:
        model = ExaminationTemplate
        fields = [
            "id",
            "name",
            "description",
            # "groups_indicators",
            "examination_template_indicators",
        ]
