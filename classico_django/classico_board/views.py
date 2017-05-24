from django.template.loader import get_template
from django.http import HttpResponse
from classico_board.forms import BoardForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView)

from classico_board.models import Board


class AboutView(TemplateView):
    template_name = 'about.html'


class BoardListView(ListView):
    model = Board

    def get_queryset(self):
        return Board.objects.order_by(Board.id)
        # return Board.objects.filter(published_date__lte='2006-01-01')
        # select * from blog_entry where published_date <= '2006-01-01';


class BoardDetailView(DetailView):
    model = Board


class BoardCreateView(LoginRequiredMixin, CreateView):
    model = Board
    form_class = BoardForm
    login_url = '/login/'
    redirect_field_name = 'board/board_detail.html'


class BoardUpdateView(LoginRequiredMixin, UpdateView):
    model = Board
    success_url = reverse_lazy('board_list')


class BoardDeleteView(LoginRequiredMixin, DeleteView):
    login_url = '/login/'
    redirect_field_name = 'board/board_detail.html'
    form_class = BoardForm
    model = Board


class DraftListView(LoginRequiredMixin,ListView):
    login_url = '/login/'
    redirect_field_name = 'board/board_list.html'
    model = Board

    def get_queryset(self):
        return Board.objects.order_by(Board.id)
        # return Board.objects.filter(published_date__isnull=True).ordey_by('createdDate')


def board_index(request):
    return HttpResponse("board_index : Hello. Board.API")


def board_list(request):
    template = get_template('classico_app/board/board_list.html')
    my_dict = {'board_list': Board.objects.all()}
    return HttpResponse(template.render(my_dict))