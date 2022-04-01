from django.shortcuts import render, redirect

def home(request):
    context = {}
    return render(request, 'base/home.html', context)

# def room(request):
#     context = {}
#     return render(request, 'base/room.html' context)
