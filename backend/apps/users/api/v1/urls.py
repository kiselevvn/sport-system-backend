from django.urls import include, path

from ... import views

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
    )
]
