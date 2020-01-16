from django.urls import path

from . import views

urlpatterns = [
    path('', views.memeView, name='index'),
    path('download',views.downloadView,name = 'download')
]
