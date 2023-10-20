from django.urls import include, path

from .v1 import views

urlpatterns = [
    path(
        "sportsman/",
        include(
            [
                path("create/", views.SportsmanCreateAPIView.as_view()),
                path("page/", views.SportsmanPageAPIView.as_view()),
                path(
                    "detail/<int:pk>/",
                    views.SportsmanRetrieveAPIView.as_view(),
                ),
            ]
        ),
    ),
    path(
        "employee/",
        include(
            [
                path("create/", views.EmployeeCreateAPIView.as_view()),
                path("page/", views.EmployeePageAPIView.as_view()),
                path(
                    "detail/<int:pk>/",
                    views.EmployeeRetrieveAPIView.as_view(),
                ),
            ]
        ),
    ),
]
