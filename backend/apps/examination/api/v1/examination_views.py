from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response

from backend.apps.examination.selectors import ExaminationSelectors
from backend.apps.examination.serializers import ExaminationSerializer


class ExaminationViewSet(viewsets.ViewSet):
    """ """

    def list(self, request):
        queryset = ExaminationSelectors.all()
        serializer = ExaminationSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = ExaminationSelectors.all()
        instance = get_object_or_404(queryset, pk=pk)
        serializer = ExaminationSerializer(instance)
        return Response(serializer.data)
