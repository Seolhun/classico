from django.conf.urls import url
from classico_app import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
]