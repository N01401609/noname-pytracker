from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('PyTraker/sign_up/', views.sign_up, name="sign_up"),
    path("PyTraker/logged_out", views.log_out, name="logout"),
    #path("PyTraker/invoice/<int:invoices_id>/", views.invoice_details, name ="invoice_details"),
    path("PyTraker/invoice", views.invoice, name="invoice"),

]