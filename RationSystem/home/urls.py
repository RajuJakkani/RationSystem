from django.contrib import admin
from . import views
from django.urls import path

urlpatterns = [
   
    path("", views.index, name="index"),
    path("grains/", views.grain, name="index"),
    path("members/", views.members, name="index"),
    path("shopkeeper", views.shopkeeper, name="shopkeeper"),
    path("client/", views.client, name="shopkeeper"),
    path("feedback", views.Feedback, name="feedback"),
    path("history", views.history, name="history"),

    # OPT Verification
    path("verification", views.verification, name="verification"),
]
