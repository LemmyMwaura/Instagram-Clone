from django.shortcuts import render, redirect
from .models import Post, Profile, Like, Comment

def home(request):
    posts = Post.objects.all()

    context = {'posts': posts}
    return render(request, 'base/home.html', context)

def room(request):
    context = {}
    return render(request, 'base/room.html', context)
