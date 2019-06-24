from django.conf.urls import url
from . import views


urlpatterns = [

    url(r'^$', views.view_music, name='index'),
    url(r'^view_music$', views.view_music, name='view_music'),
    url('add', views.add, name='add'),
    url('delete', views.delete, name='delete')

]
