from audioop import reverse

from django.shortcuts import render
from classico_app.forms import UserForm, UserProfileForm

from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request,'classico_app/index.html')


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


@login_required
def special(request):
    return HttpResponse("You are logged in, Nice!")


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
    return render(request, 'classico_app/user/register.html', {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})


def user_login(request):
    if request == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        # check auth
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active():
                login(request, user)
                return HttpResponseRedirect(reverse("index"))

            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            print("Someone tried to login and failed!!")
            print("Username : {} and Password {}".format(username, password))
            return HttpResponse("Invalid login details supplied!!")
    else:
        return render(request, 'classico_app/user/login.html')
