from django.shortcuts import render

# Create your views here.
from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.contrib.contenttypes.models import ContentType
from rest_framework import generics, permissions
from .models import Notification
from .models import Post, Like
from notifications.models import Notification
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from .serializers import NotificationSerializer


User = get_user_model()

# Implement Like Functionality

class LikePostView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        user = request.user

        # Prevent duplicate likes
        like, created = Like.objects.get_or_create(user=user, post=post)

        if not created:
            return Response({"message": "You have already liked this post."},
                            status=status.HTTP_400_BAD_REQUEST)

        #  Create notification for the post author
        if post.author != user:
            Notification.objects.create(
                recipient=post.author,
                actor=user,
                verb="liked your post",
                target=post,
                target_content_type=ContentType.objects.get_for_model(Post),
                target_object_id=post.id
            )

        return Response({"message": "Post liked successfully."},
                        status=status.HTTP_201_CREATED)


class UnlikePostView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, post_id):
        user = request.user
        post = get_object_or_404(Post, id=post_id)

        #  Remove like if it exists
        deleted, _ = Like.objects.filter(user=user, post=post).delete()

        if deleted == 0:
            return Response({"message": "You haven't liked this post."},
                            status=status.HTTP_400_BAD_REQUEST)

        return Response({"message": "Post unliked successfully."},
                        status=status.HTTP_200_OK)
    
    # Likes Notifications 

    # create notification if liking someone else’s post
if post.author != user:
    Notification.objects.create(
        recipient=post.author,
        actor=user,
        verb="liked your post",
        target=post,
        target_content_type=ContentType.objects.get_for_model(Post),
        target_object_id=post.id
    )

# Comments Notifications 

def perform_create(self, serializer):
    comment = serializer.save(author=self.request.user)

    # Notify post author
    post = comment.post
    if post.author != self.request.user:
        Notification.objects.create(
            recipient=post.author,
            actor=self.request.user,
            verb="commented on your post",
            target=comment,
            target_content_type=ContentType.objects.get_for_model(comment),
            target_object_id=comment.id
        )

        class NotificationListView(generics.ListAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Fetch only the notifications for the logged-in user
        return Notification.objects.filter(
            recipient=self.request.user
        ).order_by('-timestamp')

