from django.urls import path
from . import views

urlpatterns = [
    path('', views.home , name='home'),
    path('create_post/', views.create_post, name='create-post'),
    path('update_post/<str:pk>/', views.update_post, name='update-post'),
    path('delete_post/<str:pk>/', views.delete_post, name='delete-post'),
    path('login/', views.login_page, name='login-page'),
    path('register/', views.register_user, name='register')
]