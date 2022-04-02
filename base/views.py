from django.shortcuts import render, redirect
from .models import Post, Profile, Like, Comment
from django.db.models import Q

def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    posts = Post.objects.filter(
        Q(caption__icontains = q) |
        Q(image_name__icontains = q) |
        Q(author__username__icontains = q)
    )

    context = { 'posts': posts }
    return render(request, 'base/home.html', context)

def room(request):
    context = {}
    return render(request, 'base/room.html', context)
