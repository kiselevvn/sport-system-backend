# from django.urls import include, path

from rest_framework.routers import DefaultRouter

from ..services import NpService

# from .v1 import (

# )

router = DefaultRouter()


NpService.register_endpoints(router)


urlpatterns = [
    # path("path/", views..as_view()),
]

urlpatterns += router.urls
