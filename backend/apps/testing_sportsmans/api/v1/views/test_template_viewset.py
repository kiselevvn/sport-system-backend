from rest_framework import mixins, viewsets
from rest_framework.decorators import action

from backend.apps.testing_sportsmans.selectors import TestTemplateSelector
from backend.apps.testing_sportsmans.serializers import (
    TestTemplateCreateSerializer,
    TestTemplateListSerializer,
    TestTemplateRetrieveSerializer,
)
from backend.apps.testing_sportsmans.services import TestTemplateCreate


class TestTemplateViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    """
    Набор представлений
    Шаблон тестирования
    """

    def get_serializer_class(self):
        serializers = {
            "list": TestTemplateListSerializer,
            "retrieve": TestTemplateRetrieveSerializer,
            "create": TestTemplateCreateSerializer,
            # "update": TestTemplateCreateSerializer,
            "partial_update": TestTemplateCreateSerializer,
        }
        if self.action in serializers:
            return serializers[self.action]
        return super().get_serializer_class()

    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        # serializer.save()
        TestTemplateCreate.execute({"validated_data": serializer.data})

    def perform_update(self, serializer):
        serializer.save()

    # def get_permissions(self):
    #     if self.action in ("select",):
    #         permission_classes = [
    #             IsSportsman,
    #         ]
    #     else:
    #         permission_classes = []

    #     return [permission() for permission in permission_classes]

    def get_object(self):
        return TestTemplateSelector.base_queryset().get(
            pk=self.kwargs[self.lookup_field],
        )

    def get_queryset(self):
        return TestTemplateSelector.base_queryset()

    @action(detail=True, methods=("post",), url_path="question-create")
    def question_create(self, request, *args, **kwargs):
        return super().create(request)

    @action(detail=True, methods=("post",), url_path="question-update")
    def question_update(self, request, *args, **kwargs):
        return super().create(request)