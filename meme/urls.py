from django.urls import path

from . import views

urlpatterns = [
    path('', views.memeView, name='index'),
]
