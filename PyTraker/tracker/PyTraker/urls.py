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
    #path("PyTraker/invoice/<int:invoices_id>/", views.invoice_details, name ="invoice_details"),
    path("PyTraker/invoice/<int:invoices_id>/", views.invoice, name="invoice"),
    path("PyTraker/comments/<int:comment_id>/", views.comment_detail_view, name="comment_detail"),
    path("PyTraker/comments/", views.comment_create_view, name="comment-add"),
    path("PyTraker/comments/<int:comment_id>/delete/", views.comment_delete, name="comment_delete")

]