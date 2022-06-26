from rest_framework.serializers import ModelSerializer
from rest_framework.generics import RetrieveAPIView
from backend.apps.examination_templates.models import Indicator


class RetrieveIndicatorSerializer(ModelSerializer):
    class Meta:
        model = Indicator
        fields = ["id", "name", "description", "type_indicator", "unit"]


class RetrieveIndicatorAPIView(RetrieveAPIView):
    """
    Retrieve Indicator
    """

    serializer_class = RetrieveIndicatorSerializer
    queryset = Indicator.objects.all()
