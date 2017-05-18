from django.conf.urls import url, include
from classico_app import views

urlpatterns = [
    url(r'^$', views.index, name='board_index'),
    url(r'^list/', views.board_list, name='board_list'),
]
