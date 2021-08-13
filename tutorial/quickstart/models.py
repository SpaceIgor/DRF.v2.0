from django.db import models
from django.utils import timezone


class Category(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name


class Post(models.Model):
    post_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', default=timezone.now)
    opened = models.BooleanField(default=True)
    categories = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.post_text

    class Meta:
        ordering = ['post_text']


class Comment(models.Model):
    comment_text = models.TextField(max_length=1000)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('date published', default=timezone.now)

    def __str__(self):
        return self.comment_text
