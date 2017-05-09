from django.conf.urls import url
from . import views

app_name = "portal"
urlpatterns = [

    url(r'^$', views.index, name='index'),
    #url(r'^login/$', views.login, name='login'),
    #url(r'^registre/$', views.registre, name='registre'),
    #url(r'^logout/$', views.logout, name='logout'),
    #url(r'^contacte/$', views.contacte, name='contacte'),
]