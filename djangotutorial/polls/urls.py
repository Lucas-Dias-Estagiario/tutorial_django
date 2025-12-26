from django.urls import path

from . import views
import include

urlpatterns = [
    path("", views.index, name="index"),
]