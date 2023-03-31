from django.urls import path

from cantact_app import views

urlpatterns = [
    path('',views.addcantact),
    ]
