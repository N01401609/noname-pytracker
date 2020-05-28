from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="home"),
    path('PyTraker/sign_up/', views.sign_up, name="sign_up"),
    path("PyTraker/logged_out", views.log_out, name="logout")
]