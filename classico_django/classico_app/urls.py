from django.conf.urls import url, include
from classico_app import views

urlpatterns = [
    url(r'^index/', views.board_index, name='board_index'),
]
