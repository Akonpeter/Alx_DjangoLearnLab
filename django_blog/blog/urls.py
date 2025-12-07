from django.urls import path

from . views import( 
    CommentCreateView,
    CommentUpdateView,
    CommentDeleteView,
    ) 
from .views import RegisterView, CustomLoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("profile/", views.profile, name="profile"),
     
      path("posts/<int:post_id>/comments/new/", CommentCreateView.as_view(), name="comment_create"),

    # Edit a comment
    path("comments/<int:pk>/edit/", CommentUpdateView.as_view(), name="comment_edit"),

    # Delete a comment
    path("comments/<int:pk>/delete/", CommentDeleteView.as_view(), name="comment_delete"),
]
    

