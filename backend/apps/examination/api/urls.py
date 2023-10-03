# from django.urls import include, path

from rest_framework.routers import DefaultRouter

from .v1 import ExaminationTemplateViewSet, ExaminationViewSet

router = DefaultRouter()

router.register(
    r"examination-template",
    ExaminationTemplateViewSet,
    basename="examination-template",
)

router.register(r"examination", ExaminationViewSet, basename="examination")

urlpatterns = [
    # path("all/", views.AllExaminationTemplatesAPIView.as_view()),
]

urlpatterns += router.urls
