from django.urls import path

from . import views


urlpatterns = [
    path("status/", views.TestIsUp.as_view(), name="test_is_up"),
]
