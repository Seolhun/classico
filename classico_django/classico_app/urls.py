from django.conf.urls import url, include
from classico_app import views

app_name = 'classico_app'

urlpatterns = [
    # suffix : board/
    url(r'^index/', views.index, name='board_index'),
    url(r'^list/', views.board_list, name='boardlist'),
]
