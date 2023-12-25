from rest_framework.serializers import ModelSerializer

from backend.apps.examination.models import Indicator


class IndicatorSerializer(ModelSerializer):
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
