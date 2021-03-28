from rest_framework.serializers import ModelSerializer
from backend.apps.examination_templates.models import Indicator
from backend.apps.services.views import ProxyServiceCreateAPIView
from backend.apps.examination_templates.services import CreateIndicator


class CreateIndicatorSerializer(ModelSerializer):
    class Meta:
        model = Indicator
        fields = ["id", "name", "description", "type_indicator", "unit"]


class CreateIndicatorAPIView(ProxyServiceCreateAPIView):
    serializer_class = CreateIndicatorSerializer
    service_class = CreateIndicator
