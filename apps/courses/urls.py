from django.conf.urls import url
from . import views
# from django.contrib import admin

urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'^create$', views.create, name='create'),
    url(r'^confirm/(?P<id>\d+)$', views.confirm, name='confirm'),
    url(r'^destroy(?P<id>\d+)$', views.destroy, name='destroy'),

]
