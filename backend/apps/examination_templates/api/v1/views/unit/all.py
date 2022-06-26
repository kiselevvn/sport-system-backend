from rest_framework.generics import ListAPIView
from rest_framework.serializers import ModelSerializer

from backend.apps.examination_templates.models import Unit


class AllUnitsSerializer(ModelSerializer):
    class Meta:
        model = Unit
        fields = ["id", "short_name", "name", "description"]


class AllUnitsAPIView(ListAPIView):
    serializer_class = AllUnitsSerializer
    queryset = Unit.objects.all()
