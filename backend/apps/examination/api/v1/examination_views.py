from django.shortcuts import get_object_or_404
from django_filters import rest_framework as filters
from rest_framework import generics, viewsets
from rest_framework.response import Response

from backend.apps.examination.models import Examination
from backend.apps.examination.selectors import ExaminationSelector
from backend.apps.examination.serializers import ExaminationSerializer


class ExaminationFilter(filters.FilterSet):
    name = filters.CharFilter(field_name="name", lookup_expr="icontains")
    description = filters.CharFilter(
        field_name="name", lookup_expr="description"
    )

    class Meta:
        model = Examination
        fields = ["name", "description"]


class ExaminationViewSet(viewsets.ModelViewSet):
    """ """

    serializer_class = ExaminationSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ExaminationFilter

    # def list(self, request):
    #     queryset = self.get_queryset()
    #     serializer = self.serializer_class(queryset, many=True)
    #     return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = self.get_queryset()
        instance = get_object_or_404(queryset, pk=pk)
        serializer = self.serializer_class(instance)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):
        return ExaminationSelector.all()
