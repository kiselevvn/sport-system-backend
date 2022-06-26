from rest_framework.serializers import ModelSerializer, JSONField
from rest_framework.generics import ListAPIView
from backend.apps.examination_templates.models import Indicator, Unit


class IndicatorUnitSerializer(ModelSerializer):
    class Meta:
        model = Unit
        fields = ["id", "name", "description"]


class AllIndicatorsSerializer(ModelSerializer):

    unit = IndicatorUnitSerializer()

    class Meta:
        model = Indicator
        fields = [
            "id",
            "name",
            "description",
            "type_indicator",
            "unit",
        ]


class AllIndicatorsAPIView(ListAPIView):
    serializer_class = AllIndicatorsSerializer
    queryset = Indicator.objects.all()
