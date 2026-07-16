from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("apply/", views.apply_leave, name="apply_leave"),
    path("success/", views.success, name="success"),
]