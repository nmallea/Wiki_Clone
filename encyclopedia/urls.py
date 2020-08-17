from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.entry, name="entry"),
    path("search", views.search, name="search"),
    path("create_entry", views.create, name="create"),
    path("edit)_entry", views.edit, name="edit"),
    ]

