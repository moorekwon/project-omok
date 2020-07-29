from django.urls import path

from omok import views

urlpatterns = [
    path('', views.index, name='index'),
]