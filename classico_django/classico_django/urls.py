"""classico_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import include, url
from classico_app import views as views_user
from classico_board import views as views_board
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    # Domain Main index
    url(r'^$', views_board.board_index, name='index'),

    # App ADMIN URL
    url(r'^admin/', admin.site.urls),

    # Main App URL include
    url(r'^classico_app/', include('classico_app.urls')),
    # Board App URL include
    url(r'^classico_board/', include('classico_board.urls')),
    # Board App URL include
    url(r'^classico_keywords/', include('classico_keywords.urls')),


    url(r'^rest-swagger/', schema_view, name='rest-swagger'),
    url(r'^rest-api/', include('rest_framework.urls')),
]
