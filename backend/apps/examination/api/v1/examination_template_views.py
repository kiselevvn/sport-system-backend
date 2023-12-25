from django.shortcuts import get_object_or_404
from django_filters import rest_framework as filters
from rest_framework import viewsets
from rest_framework.response import Response

from backend.apps.examination.models import ExaminationTemplate
from backend.apps.examination.selectors import ExaminationTemplateSelector
from backend.apps.examination.serializers import ExaminationTemplateSerializer

# class ExaminationTemplateFilter(filters.FilterSet):
#     name = filters.CharFilter(field_name="name", lookup_expr="icontains")
#     description = filters.CharFilter(
#         field_name="name", lookup_expr="description"
#     )

#     class Meta:
#         model = ExaminationTemplate
#         fields = ["name", "description"]


class ExaminationTemplateViewSet(viewsets.ModelViewSet):
    """
    Шаблоны обследований
    """

    queryset = ExaminationTemplateSelector.all()
    serializer_class = ExaminationTemplateSerializer
    # filter_backends = (filters.DjangoFilterBackend,)
    # filterset_class = ExaminationTemplateFilter

    # def list(self, request):
    #     queryset = ExaminationTemplateSelector.all()
    #     serializer = ExaminationTemplateSerializer(queryset, many=True)
    #     return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = ExaminationTemplateSelector.all()
        instance = get_object_or_404(queryset, pk=pk)
        serializer = ExaminationTemplateSerializer(instance)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save()
