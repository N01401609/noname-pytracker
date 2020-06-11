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

    path("PyTraker/invoice/<int:invoices_id>/", views.invoice, name="invoice"),
    path("PyTraker/list_invoices/", views.invoice_list, name="list_invoices"),
    path("PyTraker/new_invoice/", views.new_invoice, name="new_invoice"),
    path("PyTraker/edit_invoice/<int:invoices_id>/", views.edit_invoice, name="edit_invoice"),
    path("PyTraker/comments/<int:comment_id>/", views.comment_detail_view, name="comment_detail"),
    path("PyTraker/comments/", views.comment_create_view, name="comment-add"),
    path("PyTraker/comments/<int:comment_id>/delete/", views.comment_delete, name="comment_delete"),
    path("PyTraker/tasklist", views.tasklist, name="tasklist"),
    path("PyTraker/task_detail", views.task_detail, name="task_detail"),
    path("PyTraker/projects", views.projects, name="projects"),
    path("PyTraker/project_detail", views.project_detail, name="project_detail"),
    path("PyTraker/new_project", views.new_project, name="new_project"),
    path("PyTraker/edit_project/<int:pk>", views.edit_project, name="edit_project"),
    path("PyTraker/details_project/<int:pk>", views.details_project, name="details_project"),
    path("PyTraker/delete_project/<int:pk>", views.delete_project, name="delete_project"),
    path("PyTraker/list_projects", views.list_projects, name="list_projects"),
    path("PyTraker/workdiary", views.workdiary, name="workdiary"),
    path("PyTraker/workdiary_add", views.workdiary_add, name="workdiary_add"),
    path("PyTraker/workdiary_edit/<int:pk>", views.workdiary_edit, name="workdiary_edit"),
    path("PyTraker/workdiary_detail/<int:pk>", views.workdiary_details, name="workdiary_detail"),
    path("PyTraker/workdiary_delete/<int:pk>", views.workdiary_delete, name="workdiary_delete"),
    path("PyTraker/workdiary_conf_delete/<int:pk>", views.workdiary_conf_delete, name="workdiary_conf_delete")

]
