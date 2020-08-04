from django.shortcuts import render


def index(request):
    return render(request, 'omok/index.html')


def put_stone(request, room_name):
    print(request)
    return render(request, 'omok/data.html', {'room_name': room_name})
