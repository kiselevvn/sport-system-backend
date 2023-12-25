# from django.urls import include, path

from rest_framework.routers import DefaultRouter

from .v1 import (
    ExaminationTemplateIndicatorsViewSet,
    ExaminationTemplateViewSet,
    ExaminationViewSet,
    GroupIndicatorsViewSet,
    IndicatorViewSet,
)

router = DefaultRouter()

router.register(
    r"examination-template",
    ExaminationTemplateViewSet,
    basename="examination-template",
)
router.register(
    r"examination-template-indicators",
    ExaminationTemplateIndicatorsViewSet,
    basename="examination-template-indicators",
)
router.register(r"examination", ExaminationViewSet, basename="examination")
router.register(
    r"group-indicators", GroupIndicatorsViewSet, basename="group-indicators"
)
router.register(r"indicator", IndicatorViewSet, basename="indicator")

urlpatterns = [
    # path("path/", views..as_view()),
]

urlpatterns += router.urls
