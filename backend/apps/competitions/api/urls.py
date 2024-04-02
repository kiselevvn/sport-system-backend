# from django.urls import path

from rest_framework.routers import DefaultRouter

from .v1 import SportCategoryViewSet, SportDisciplineViewSet

router = DefaultRouter()

router.register(
    r"sport-category",
    SportCategoryViewSet,
    basename="sport-category",
)
router.register(
    r"sport-discipline",
    SportDisciplineViewSet,
    basename="sport-discipline",
)

urlpatterns = [
    # path("all/", views.AllExaminationTemplatesAPIView.as_view()),
]

urlpatterns += router.urls
