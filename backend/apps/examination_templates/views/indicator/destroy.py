from rest_framework.generics import DestroyAPIView
from backend.apps.examination_templates.models import Indicator


class DestroyIndicatorAPIView(DestroyAPIView):
    """
    Destroy Indicator
    """

    queryset = Indicator.objects.all()
