from rest_framework.serializers import ModelSerializer
from backend.apps.examination_templates.models import Indicator
from rest_framework.generics import CreateAPIView


class CreateIndicatorSerializer(ModelSerializer):
    class Meta:
        model = Indicator
        fields = ["id", "name", "description", "type_indicator", "unit"]


class CreateIndicatorAPIView(CreateAPIView):
    serializer_class = CreateIndicatorSerializer
