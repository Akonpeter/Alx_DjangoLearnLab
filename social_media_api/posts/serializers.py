from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Post, Comment

User = get_user_model()


class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)  # shows username
    author_id = serializers.PrimaryKeyRelatedField(
        source='author',
        queryset=User.objects.all(),
        write_only=True,
        required=False
    )

    class Meta:
        model = Post
        fields = [
            'id',
            'author',
            'author_id',
            'title',
            'content',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['created_at', 'updated_at']

    def validate_title(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Title must be at least 3 characters.")
        return value


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    author_id = serializers.PrimaryKeyRelatedField(
        source='author',
        queryset=User.objects.all(),
        write_only=True,
        required=False
    )
    post_id = serializers.PrimaryKeyRelatedField(
        source='post',
        queryset=Post.objects.all(),
        write_only=True
    )

    class Meta:
        model = Comment
        fields = [
            'id',
            'post',
            'post_id',
            'author',
            'author_id',
            'content',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['created_at', 'updated_at', 'post']

    def validate_content(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Comment cannot be empty.")
        return value
