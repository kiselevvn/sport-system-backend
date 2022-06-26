from django.urls import include, path

from . import views

urlpatterns = [
    path(
        "",
        include([
            path("all/", views.AllExaminationTemplatesAPIView.as_view()),
            path("retrive/<int:pk>/", views.RetrieveExaminationTemplateAPIView.as_view()),
            path("create/", views.CreateExaminationTemplateAPIView.as_view()),
            path("create-group/<int:pk>/", views.ExaminationTemplateCreateGroupAPIView.as_view()),
        ])
    ),
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
