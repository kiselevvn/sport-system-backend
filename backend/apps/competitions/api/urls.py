# from django.urls import path

from rest_framework.routers import DefaultRouter

from .v1 import SportTypeViewSet

router = DefaultRouter()

router.register(
    r"sport-type",
    SportTypeViewSet,
    basename="sport-type",
)


urlpatterns = [
    # path("all/", views.AllExaminationTemplatesAPIView.as_view()),
]

urlpatterns += router.urls
