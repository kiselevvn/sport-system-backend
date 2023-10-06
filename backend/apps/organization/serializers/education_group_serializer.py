from rest_framework.serializers import ModelSerializer

from backend.apps.organization.models import EducationGroup


class ResultsExaminationSerializer(ModelSerializer):
    """
    Результат обследования
    """

    class Meta:
        model = EducationGroup
        # fields = ["id", ]
        fields = "__all__"
