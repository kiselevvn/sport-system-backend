from rest_framework.serializers import ModelSerializer
from rest_framework.generics import ListAPIView
from backend.apps.examination_templates.models import ExaminationTemplate


class AllExaminationTemplatesSerializer(ModelSerializer):
    class Meta:
        model = ExaminationTemplate
        fields = ["id", "name", "description"]


class AllExaminationTemplatesAPIView(ListAPIView):
    serializer_class = AllExaminationTemplatesSerializer
    queryset = ExaminationTemplate.objects.all()
