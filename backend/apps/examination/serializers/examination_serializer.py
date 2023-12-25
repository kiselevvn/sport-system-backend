from rest_framework.serializers import ModelSerializer

from backend.apps.examination.models import (
    Examination,
    ResultExamination,
    ResultIndicator,
)


class ResultIndicatorSerializer(ModelSerializer):
    """
    Результат показателя
    """

    class Meta:
        model = ResultIndicator
        # fields = ["id", ]
        fields = "__all__"


class ResultsExaminationSerializer(ModelSerializer):
    """
    Результат обследования
    """

    results_indicators = ResultIndicatorSerializer(many=True, read_only=True)

    class Meta:
        model = ResultExamination
        # fields = ["id", ]
        fields = "__all__"


class ExaminationSerializer(ModelSerializer):
    """
    Обследование
    """

    results = ResultsExaminationSerializer(many=True, read_only=True)

    class Meta:
        model = Examination
        # fields = ["id", "name", "description", "groups_indicators"]
        fields = "__all__"
