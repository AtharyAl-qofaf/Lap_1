from django.urls import path
from . import views

app_name = 'doctors'

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("add/", views.doctor_create, name="doctor_create"),
    path("<int:doctor_id>/edit/", views.doctor_update, name="doctor_update"),
    path("<int:doctor_id>/delete/", views.doctor_delete, name="doctor_delete"),
    path("<int:doctor_id>/", views.detail, name="detail"),
]