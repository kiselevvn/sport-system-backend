from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response

from backend.apps.competitions.selectors import ExaminationTemplateSelectors
from backend.apps.competitions.serializers import SportTypeSerializer


class SportTypeViewSet(viewsets.ModelViewSet):
    """ """

    serializer_class = SportTypeSerializer

    def list(self, request):
        queryset = ExaminationTemplateSelectors.all()
        serializer = SportTypeSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = ExaminationTemplateSelectors.all()
        instance = get_object_or_404(queryset, pk=pk)
        serializer = SportTypeSerializer(instance)
        return Response(serializer.data)
