# from django.shortcuts import get_object_or_404
# from django_filters import rest_framework as filters
from rest_framework import viewsets

from backend.apps.examination.models import ExaminationTemplateIndicators

# from backend.apps.examination.selectors import ExaminationTemplateSelector
from backend.apps.examination.serializers import (
    ExaminationTemplateIndicatorsSerializer,
)

# from rest_framework.response import Response


class ExaminationTemplateIndicatorsViewSet(viewsets.ModelViewSet):
    """
    Группа показателей
    """

    queryset = ExaminationTemplateIndicators.objects.all()
    serializer_class = ExaminationTemplateIndicatorsSerializer

    # def retrieve(self, request, pk=None):
    #     queryset = ExaminationTemplateSelector.all()
    #     instance = get_object_or_404(queryset, pk=pk)
    #     serializer = GroupIndicatorsSerializer(instance)
    #     return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save()
