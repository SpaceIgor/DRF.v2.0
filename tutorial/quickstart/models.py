from django.db import models


class Post(models.Model):
    post_text = models.CharField(max_length=200)
    opened = models.BooleanField(default=True)

    def __str__(self):
        return self.post_text


class Comment(models.Model):
    comment_text = models.TextField(max_length=1000)
    comments = models.ManyToManyField(Post)

    def __str__(self):
        return self.comment_text


class Category(models.Model):
    category_text = models.CharField(max_length=200)
    category_name = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.category_text
