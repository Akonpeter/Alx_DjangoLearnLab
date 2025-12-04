# blog/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import register, profile

urlpatterns = [
    # Built-in authentication views
    path('login/', auth_views.LoginView.as_view(template_name='blog/registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/registration/logout.html'), name='logout'),
    path('password-change/', auth_views.PasswordChangeView.as_view(template_name='blog/registration/password_change.html'), name='password_change'),
    path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='blog/registration/password_change_done.html'), name='password_change_done'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='blog/registration/password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='blog/registration/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='blog/registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='blog/registration/password_reset_complete.html'), name='password_reset_complete'),
    
    # Custom views
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    
    # Blog views
    path('', views.post_list, name='post_list'),
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
]