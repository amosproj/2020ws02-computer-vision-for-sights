"""This module contains the URLs exposed by the api subapp."""
from django.urls import path
from . import views

urlpatterns = [
    path("cities/<city>/image", views.persist_sight_image, name="persist_sight_image"),
    path("cities/<city>/model", views.get_trained_city_model, name="get_trained_city_model"),
    path("cities/<city>/model/version", views.get_latest_city_model_version, name="get_latest_city_model_version"),
    path("cities/", views.get_supported_cities, name="get_supported_cities"),
    path("cities/<city>/add", views.add_new_city, name="add_new_city"),
    path("", views.get_index, name="get_index")
]
