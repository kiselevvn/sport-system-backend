from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response

from backend.apps.examination.selectors import ExaminationTemplateSelector
from backend.apps.examination.serializers import ExaminationTemplateSerializer


class ExaminationTemplateViewSet(viewsets.ModelViewSet):
    """ """

    serializer_class = ExaminationTemplateSerializer

    def list(self, request):
        queryset = ExaminationTemplateSelector.all()
        serializer = ExaminationTemplateSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = ExaminationTemplateSelector.all()
        instance = get_object_or_404(queryset, pk=pk)
        serializer = ExaminationTemplateSerializer(instance)
        return Response(serializer.data)
