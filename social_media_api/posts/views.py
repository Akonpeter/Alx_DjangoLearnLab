from rest_framework import viewsets, permissions, filters, generics
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from .permissions import IsAuthorOrReadOnly

User = get_user_model()

def get_object(self):
        obj = get_object_or_404(Post, pk=self.kwargs['pk'])

#   POST VIEWSET

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
     
     
     
    # Enable search + ordering
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'content']
    ordering_fields = ['created_at', 'updated_at', 'title']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

        



#   COMMENT VIEWSET

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)



#   FEED VIEW

class FeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        followed_users = self.request.user.following.all()
        return Post.objects.filter(author__in=followed_users).order_by('-created_at')

["generics.get_object_or_404(Post, pk=pk)",
  "Like.objects.get_or_create(user=request.user, post=post)",
  "Notification.objects.create"]