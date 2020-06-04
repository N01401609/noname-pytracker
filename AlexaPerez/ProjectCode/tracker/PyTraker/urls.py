from django.contrib import admin
from django.urls import path
from . import views

app_name = 'PyTraker'
urlpatterns = [
    path('', views.home, name="home"),
    path('PyTraker/index', views.home, name="home"),
    path('PyTraker/sign_up/', views.sign_up, name="sign_up"),
    path('PyTraker/login', views.login_page, name="login"),
    path("PyTraker/logout", views.log_out, name="logout"),

]
