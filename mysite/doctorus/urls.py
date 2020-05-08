from django.urls import path

from . import views

from django.conf.urls import url

app_name = 'doctorus'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    
]
