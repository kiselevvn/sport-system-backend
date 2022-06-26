from rest_framework.generics import CreateAPIView
from rest_framework.serializers import ModelSerializer

from backend.apps.examination_templates.models import Unit


class CreateUnitSerializer(ModelSerializer):
    class Meta:
        model = Unit
        fields = ["id", "short_name", "name", "description"]


class CreateUnitAPIView(CreateAPIView):
    serializer_class = CreateUnitSerializer
