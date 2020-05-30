from django.conf.urls import url
from . import views

urlpatterns = [
    # /comments
    url(r'^$', views.index, name='index'),

    # /comments/1
    # it will show the result from the database with the id =1
    url(r'^(?P<comments_id>[0-9]+)/$',views.detail, name='detail'),
]