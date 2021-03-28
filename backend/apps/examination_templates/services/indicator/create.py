from backend.apps.services.services import ServiceBase


class CreateIndicator(ServiceBase):
    def execute(self, serializer):
        serializer.Meta.model.objects.create(**serializer.validated_data)
