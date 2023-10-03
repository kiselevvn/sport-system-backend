# from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .v1 import TestTemplateViewSet

app_name = "testing"

router = DefaultRouter()

router.register(
    "test-template",
    TestTemplateViewSet,
    basename="test-template",
)
# print(router.urls)
urlpatterns = [
    # path("all/", views.AllExaminationTemplatesAPIView.as_view()),
    *router.urls
]
