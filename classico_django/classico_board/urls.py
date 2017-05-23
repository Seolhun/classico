from django.conf.urls import url, include
from classico_board import views as views_board

app_name = 'classico_board'

urlpatterns = [
    # suffix : board/
    url(r'^index/', views_board.board_index, name='board_index'),
    url(r'^list/', views_board.board_list, name='board_list'),
]
