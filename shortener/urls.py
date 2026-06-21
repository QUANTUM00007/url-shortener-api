from django.urls import path
from .views import CreateShortURL, AnalyticsView

urlpatterns = [
    path(
        "shorten/",
        CreateShortURL.as_view(),
        name="shorten-url"
    ),

    path(
        "analytics/<str:code>/",
        AnalyticsView.as_view(),
        name="analytics"
    ),
]
