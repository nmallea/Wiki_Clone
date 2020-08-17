from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<title>", views.entry_page, name="wiki"),
    path("search/", views.search, name="search"),
    path("create_entry/", views.create_entry, name="create_entry"),
    path("edit_entry/title>", views.edit_entry, name="edit_entry"),
    ]

