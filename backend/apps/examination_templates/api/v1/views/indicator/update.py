from rest_framework.serializers import ModelSerializer
from rest_framework.generics import UpdateAPIView
from backend.apps.examination_templates.models import Indicator


class UpdateIndicatorSerializer(ModelSerializer):
    class Meta:
        model = Indicator
        fields = ["id", "name", "description", "type_indicator", "unit"]


class UpdateIndicatorAPIView(UpdateAPIView):
    """
    Update Indicator
    """

    serializer_class = UpdateIndicatorSerializer
    queryset = Indicator.objects.all()