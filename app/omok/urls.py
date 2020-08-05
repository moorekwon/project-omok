from django.urls import path

from omok import views

urlpatterns = [
    path('', views.waiting_room, name='waiting_room'),
    path('<str:room_name>/', views.game, name='game'),
    ]