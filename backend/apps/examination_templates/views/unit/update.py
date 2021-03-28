from rest_framework.serializers import ModelSerializer
from rest_framework.generics import UpdateAPIView
from backend.apps.examination_templates.models import Unit


class UpdateUnitSerializer(ModelSerializer):
    class Meta:
        model = Unit
        fields = ["id", "short_name", "name", "description"]


class UpdateUnitAPIView(UpdateAPIView):
    """
    Update Unit
    """

    serializer_class = UpdateUnitSerializer
    queryset = Unit.objects.all()