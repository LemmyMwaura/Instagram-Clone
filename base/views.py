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

def user_profile(request,pk):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    user = Profile.objects.get(id=pk)
    posts = user.post_set.all()
    followers = user.followers.all()
    following = user.following.all()

    context = { 'user':user, 'posts':posts, 'followers':followers, 'following':following, }
    return render(request, 'base/profile.html', context)

@login_required(login_url='login')
def follow_toggle(request, pk):
    user_profile = User.objects.get(id=pk)
    followers = user_profile.followers.all()

    current_user = User.objects.get(id=request.user.id)
    following = current_user.following.all()

    print(user_profile)
    print(current_user)
    print('following ->', following)
    print('followers ->', followers)

    if user_profile != current_user:
        new_follower = Profile.objects.get(id=pk)
        now_following = Profile.objects.get(id=request.user.id)
        if current_user in followers:
            new_follower.followers.remove(current_user.id)
            print('followers ->', followers)
        else:
            new_follower.followers.add(current_user.id)
            print('followers ->', followers)

        if user_profile in following:
            now_following.followers.remove(current_user.id)
            print('following ->', following)
        else:
            now_following.followers.add(current_user.id)
            print('following ->', following)


    return HttpResponseRedirect(reverse('profile', args=[user_profile.id]))