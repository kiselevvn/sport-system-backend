from rest_framework.serializers import ModelSerializer

from backend.apps.examination.models import GroupIndicators


class GroupIndicatorsSerializer(ModelSerializer):
    """
    Группа показателей
    """

    class Meta:
        model = GroupIndicators
        # fields = ["id", "name", "description", "indicators"]
        fields = "__all__"
