from rest_framework.generics import RetrieveAPIView
from rest_framework.serializers import ModelSerializer

from backend.apps.examination_templates.models import Unit


class RetrieveUnitSerializer(ModelSerializer):
    class Meta:
        model = Unit
        fields = ["id", "short_name", "name", "description"]


class RetrieveUnitAPIView(RetrieveAPIView):
    """
    Retrieve Unit
    """

    serializer_class = RetrieveUnitSerializer
    queryset = Unit.objects.all()
