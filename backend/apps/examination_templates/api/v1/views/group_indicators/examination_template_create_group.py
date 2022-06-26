from rest_framework.serializers import ModelSerializer
from rest_framework.generics import CreateAPIView
from backend.apps.examination_templates.models import (
    GroupIndicators,
    ExaminationTemplate,
)


class ExaminationTemplateCreateGroupSerializer(ModelSerializer):
    class Meta:
        model = GroupIndicators
        fields = ["id", "name", "description"]


class ExaminationTemplateCreateGroupAPIView(CreateAPIView):
    serializer_class = ExaminationTemplateCreateGroupSerializer

    def perform_create(self, serializer):
        assert self.kwargs["pk"] is not None
        examination_template = ExaminationTemplate.objects.get(
            pk=self.kwargs["pk"]
        )
        obj = serializer.save()
        examination_template.groups_indicators.add(obj)