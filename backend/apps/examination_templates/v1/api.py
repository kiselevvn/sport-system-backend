from django.urls import path, include
from .. import views


urlpatterns = [
    path(
        "indicator/",
        include(
            [
                path("all/", views.AllIndicatorsAPIView.as_view()),
                path("create/", views.CreateIndicatorAPIView.as_view()),
                path(
                    "update/<int:pk>/", views.UpdateIndicatorAPIView.as_view()
                ),
                path(
                    "retrive/<int:pk>/",
                    views.RetrieveIndicatorAPIView.as_view(),
                ),
                path(
                    "destroy/<int:pk>/",
                    views.DestroyIndicatorAPIView.as_view(),
                ),
            ]
        ),
    ),
    path(
        "unit/",
        include(
            [
                path("all/", views.AllUnitsAPIView.as_view()),
                path("create/", views.CreateUnitAPIView.as_view()),
                path("update/<int:pk>/", views.UpdateUnitAPIView.as_view()),
                path(
                    "retrieve/<int:pk>/", views.RetrieveUnitAPIView.as_view()
                ),
                path("destroy/<int:pk>/", views.DestroyUnitAPIView.as_view()),
            ]
        ),
    ),
]
