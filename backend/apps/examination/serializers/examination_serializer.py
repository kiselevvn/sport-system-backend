from rest_framework.serializers import ModelSerializer

from backend.apps.examination.models import Examination, ResultExaminations


class ResultsExaminationSerializer(ModelSerializer):
    """
    Результат обследования
    """

    class Meta:
        model = ResultExaminations
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
