from rest_framework.generics import DestroyAPIView
from backend.apps.examination_templates.models import Unit


class DestroyUnitAPIView(DestroyAPIView):
    """
    Destroy Unit
    """

    queryset = Unit.objects.all()
