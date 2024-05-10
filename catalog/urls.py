from django.contrib import admin
from django.urls import path, include
from catalog.apps import CatalogConfig
from catalog.views import home

app_name = CatalogConfig.name

urlpatterns = [
    path('catalog/', home, name="catalog")
]