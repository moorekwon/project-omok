from django.urls import path

from omok import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:room_name>/', views.put_stone, name='put_stone'),
    ]