from django.shortcuts import render


def waiting_room(request):
    return render(request, 'omok/waiting_room.html')


def game(request, room_name):
    return render(request, 'omok/game.html', {'room_name': room_name})
