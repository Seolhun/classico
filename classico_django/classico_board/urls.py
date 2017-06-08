from django.conf.urls import url
from classico_board import views as views_board

app_name = 'classico_board'

urlpatterns = [
    # suffix : board/
    url(r'^$', views_board.board_index, name='board_list'),
    url(r'^about/', views_board.AboutView.as_view(), name='about'),
    url(r'^detail/(?P<pk>\d+)$', views_board.BoardDetailView.as_view(), name='board_detail'),
    url(r'^create/$', views_board.BoardCreateView.as_view(),name='board_create'),
    url(r'^(?P<pk>\d+)/update/$', views_board.BoardUpdateView.as_view(),name='board_update'),
    url(r'^(?P<pk>\d+)/delete/$', views_board.BoardDeleteView.as_view(),name='board_delete'),
    url(r'^drafts/$', views_board.DraftListView.as_view(),name='board_draft_list'),
]
