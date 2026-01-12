from django.urls import path
from .views import FollowUserView, UnfollowUserView
from .views import (
    UserRegistrationView,
    LoginView,
    UserProfileView
)

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name="register"),
    path('login/', LoginView.as_view(), name="login"),
    path('profile/', UserProfileView.as_view(), name="profile"),
    path('follow/<int:user_id>/', FollowUserView.as_view(), name="follow-user"),
    path('unfollow/<int:user_id>/', UnfollowUserView.as_view(), name="unfollow-user"),
]




