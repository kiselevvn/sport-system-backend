from rest_framework.serializers import ModelSerializer
from rest_framework.generics import CreateAPIView
from backend.apps.examination_templates.models import ExaminationTemplate


class CreateExaminationTemplateSerializer(ModelSerializer):
    class Meta:
        model = ExaminationTemplate
        fields = ["id", "name", "description"]


class CreateExaminationTemplateAPIView(CreateAPIView):
    serializer_class = CreateExaminationTemplateSerializer
