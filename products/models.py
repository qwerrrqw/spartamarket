from django.db import models
from django.conf import settings


class Hashtag(models.Model):
    content = models.CharField(max_length=30, unique=True)
    # articles = models.ManyToManyField('Article', related_name='hashtag_articles')

    def __str__(self):
        return self.content


class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to="images/", blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="articles")
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_articles")
    hashtags = models.ManyToManyField(Hashtag, blank=True, related_name='article_hashtags')

    def __str__(self):
        return self.title
