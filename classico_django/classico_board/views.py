from django.template.loader import get_template

from classico_board.models import Board

from django.http import HttpResponse


def board_index(request):
    return HttpResponse("board_index : Hello. Board.API")


def board_list(request):
    template = get_template('classico_app/board/board_list.html')
    my_dict = {'board_list': Board.objects.all()}
    return HttpResponse(template.render(my_dict))