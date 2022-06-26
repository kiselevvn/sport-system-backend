from rest_framework.generics import DestroyAPIView
from backend.apps.examination_templates.models import ExaminationTemplate


class DestroyExaminationTemplateAPIView(DestroyAPIView):
    """
    Destroy ExaminationTemplate
    """

    queryset = ExaminationTemplate.objects.all()
