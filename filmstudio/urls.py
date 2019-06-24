from django.conf.urls import url
from . import views
from django.urls import path
from django.contrib import admin

urlpatterns = [
        url(r'^$', views.home, name='home'),



]
