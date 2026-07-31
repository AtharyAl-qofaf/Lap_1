from django.urls import path
from . import views

app_name = 'doctors'

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("<int:doctor_id>/", views.detail, name="detail"),
]