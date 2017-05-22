from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template

from classico_app.models import Board
from classico_app.forms import UserForm, UserProfileForm


def index(request):
    my_dict = {'insert_me': "Now I am coming from classico_app/index.html"}
    return render(request, 'classico_app/index.html', context=my_dict)


def board_index(request):
    return HttpResponse("board_index : Hello. Board.API")


def board_list(request):
    template = get_template('classico_app/board_list.html')
    my_dict = {'board_list': Board.objects.all()}

    return HttpResponse(template.render(my_dict))


def register(request):

    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            # Lazy Load
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, 'classico_app/register.html', {'user_form' : user_form, 'profile_form' : profile_form, 'registered' : registered})