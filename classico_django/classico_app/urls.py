from django.conf.urls import url, include
from classico_app import views

app_name = 'classico_app'

urlpatterns = [
    url(r'^register/', views.register, name='register'),
]
