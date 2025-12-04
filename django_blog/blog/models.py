# blog/models.py - Enhanced version
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

class Post(models.Model):
    """
    Blog Post Model with additional features
    """
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)  # For URLs
    content = models.TextField()
    excerpt = models.TextField(max_length=500, blank=True)  # Short summary
    published_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)  # Updates on save
    author = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='posts'
    )
    status = models.CharField(
        max_length=10,
        choices=[
            ('draft', 'Draft'),
            ('published', 'Published'),
        ],
        default='draft'
    )
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        """Returns the URL to access a particular post instance"""
        return reverse('post_detail', kwargs={'slug': self.slug})
    
    class Meta:
        ordering = ['-published_date']
        verbose_name = 'Blog Post'
        verbose_name_plural = 'Blog Posts'