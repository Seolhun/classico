from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template

from classico_app.models import Board


def index(request):
    my_dict = {'insert_me': "Now I am coming from classico_app/index.html"}
    return render(request, 'classico_app/index.html', context=my_dict)


def board_index(request):
    return HttpResponse("board_index : Hello. Board.API")


def board_list(request):
    template = get_template('classico_app/board_list.html')
    my_dict = {'board_list': Board.objects.all()}

    return HttpResponse(template.render(my_dict))
