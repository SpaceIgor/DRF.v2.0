from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Author(models.Model):
    author_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    is_notified = models.BooleanField(default=False)

    def __str__(self):
        return self.author_name


class Post(models.Model):
    post_text = models.CharField(max_length=300)
    slug = models.SlugField(max_length=100, unique=True)
    pub_date = models.DateTimeField("date_published", default=timezone.now)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='blog_posts')
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    opened = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        ordering = ['post_text', 'author', 'category']

    def __str__(self):
        return self.post_text


class Comment(models.Model):
    text = models.TextField(max_length=700)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_comments')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='comments')
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.text


class Category(models.Model):
    category_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ['category_name']

    def __str__(self):
        return self.category_name