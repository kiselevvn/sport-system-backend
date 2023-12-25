# from django.shortcuts import get_object_or_404
# from django_filters import rest_framework as filters
from rest_framework import viewsets

from backend.apps.examination.models import Indicator

# from backend.apps.examination.selectors import ExaminationTemplateSelector
from backend.apps.examination.serializers import IndicatorSerializer

# from rest_framework.response import Response


class IndicatorViewSet(viewsets.ModelViewSet):
    """
    Показатель медицинского обследования
    """

    queryset = Indicator.objects.all()
    serializer_class = IndicatorSerializer

    # def retrieve(self, request, pk=None):
    #     queryset = ExaminationTemplateSelector.all()
    #     instance = get_object_or_404(queryset, pk=pk)
    #     serializer = GroupIndicatorsSerializer(instance)
    #     return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save()
