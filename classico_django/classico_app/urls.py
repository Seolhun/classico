from django.conf.urls import url, include
from classico_app import views as views_app

app_name = 'classico_app'

urlpatterns = [
    url(r'^user_login/$', views_app.user_login, name='user_login'),
    url(r'^register/$', views_app.register, name='register'),

]
