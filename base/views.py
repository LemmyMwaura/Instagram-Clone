from email.message import Message
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Post, Profile, Like, Comment
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from django.urls import reverse
from django.contrib import messages 
from .forms import PostForm
import os

def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    posts = Post.objects.filter(
        Q(caption__icontains = q) |
        Q(image_name__icontains = q) |
        Q(user_posts__username__icontains = q)
    )

    context = { 'posts': posts }
    return render(request, 'base/home.html', context)

def login_page(request):
    page = 'login'
    if request.user.is_authenticated:
        messages.success(request, 'Already Logged in')
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or Password does not exist.')

    context={ 'page':page }
    return render(request, 'base/login_register.html', context)

@login_required(login_url='login')
def logout_user(request):
    logout(request)
    return redirect('home')

def register_user(request):
    page = 'register'
    form = UserCreationForm

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occured during registration')

    context = { 'page':page, 'form':form }
    return render(request, 'base/login_register.html', context)

@login_required(login_url='login')
def create_post(request):
    form = PostForm()

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.author_id = request.user.id
            user.user_posts_id = request.user.id
            user.save()
            return redirect('home')

    context = { 'form':form }
    return render(request, 'base/post_form.html', context)

@login_required(login_url='login')
def update_post(request, pk):
    post = Post.objects.get(id=pk)
    form = PostForm(instance=post)

    if request.user != post.author:
        messages.error(request, 'You are not the author of the post!')
        return redirect('home')

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            print(request.POST)
            image = form.save(commit=False)
            image.save()
            return redirect('home')

    context = { 'form':form }
    return render(request, 'base/post_form.html', context)

@login_required(login_url='login')
def delete_post(request, pk):
    post = Post.objects.get(id=pk)
    
    if request.method == 'POST':
        try:
            post.delete()
            return redirect('home')
        except:
            messages.error('Post does not exist')

    context = { 'obj':post }
    return render(request, 'base/delete.html', context)

@login_required(login_url='login')
def create_comment(request, pk):
    if request.method == 'POST':
        if post := Post.objects.get(id=pk):
            message = Comment.objects.create(
                user = request.user,
                post_to_comment = post,
                body = request.POST.get('comment')
            )
        else:
            messages.error('Post does not exist' )
    else:
        messages.error('Couldn\'t create your comment, Try again' )

    return redirect('home')

def user_profile(request,pk):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    user = Profile.objects.get(id=pk)
    posts = user.post_set.all()
    followers = user.followers.all()
    following = user.following.all()

    context = { 'user':user, 'posts':posts, 'followers':followers, 'following':following, }
    return render(request, 'base/profile.html', context)

@login_required(login_url='login')
def manage_follow(request, pk):
    user_profile = Profile.objects.get(id=pk)
    all_profiles_followers = user_profile.followers.all()
    
    current_user = Profile.objects.get(id=request.user.id)
    all_current_user_is_following = current_user.following.all()

    if user_profile.id != current_user.id:   
        if current_user in all_profiles_followers:
            user_profile.followers.remove(current_user)
        else:  
            user_profile.followers.add(current_user) 

        if user_profile in all_current_user_is_following:
            current_user.following.remove(user_profile)  
        else:
            current_user.following.add(user_profile) 

    return HttpResponseRedirect(reverse('profile', args=[user_profile.id]))