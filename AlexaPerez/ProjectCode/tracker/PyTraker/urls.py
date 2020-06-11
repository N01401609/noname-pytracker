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
    path("PyTraker/workdiary", views.workdiary, name="workdiary"),
    path("PyTraker/workdiary_add", views.workdiary_add, name="workdiary_add"),
    path("PyTraker/workdiary_edit/<int:pk>", views.workdiary_edit, name="workdiary_edit"),
    path("PyTraker/workdiary_detail/<int:pk>", views.workdiary_details, name="workdiary_detail"),
    path("PyTraker/workdiary_delete/<int:pk>", views.workdiary_delete, name="workdiary_delete"),
    path("PyTraker/workdiary_conf_delete/<int:pk>", views.workdiary_conf_delete, name="workdiary_conf_delete")

]
