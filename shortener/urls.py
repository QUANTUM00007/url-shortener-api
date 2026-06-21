from django.urls import path
from .views import CreateShortURL

urlpatterns = [
    path(
        "shorten/",
        CreateShortURL.as_view(),
        name="shorten-url"
    ),
]
