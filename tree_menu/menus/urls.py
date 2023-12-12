from django.urls import re_path

from menus import views

app_name = '%(app_label)s'

urlpatterns = [
    re_path(r'^.*$', views.menus, name='menus'),
]
