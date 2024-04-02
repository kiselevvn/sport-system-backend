from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response

from backend.apps.testing.selectors import TestTemplateSelectors
from backend.apps.testing.serializers import TestTemplateSerializer


class TestTemplateViewSet(viewsets.ModelViewSet):
    """
    Набор представлений
    Шаблон тестирования
    """

    serializer_class = TestTemplateSerializer

    def list(self, request):
        queryset = TestTemplateSelectors.all()
        serializer = TestTemplateSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = TestTemplateSelectors.all()
        instance = get_object_or_404(queryset, pk=pk)
        serializer = TestTemplateSerializer(instance)
        return Response(serializer.data)
