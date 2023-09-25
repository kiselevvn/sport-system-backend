# from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .v1 import views

app_name = "testing_sportsmans"

router = DefaultRouter()

router.register(
    "test-template",
    views.TestTemplateViewSet,
    basename="test-template",
)
# print(router.urls)
urlpatterns = [
    # path("all/", views.AllExaminationTemplatesAPIView.as_view()),
    *router.urls
]
