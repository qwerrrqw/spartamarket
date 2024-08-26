from django.db import models
from django.conf import settings


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to="images/", blank=True)

    author = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="articles",
    )

    like_users = models.ManyToManyField(to=settings.AUTH_USER_MODEL, related_name="like_articles")
    # like_count = models.PositiveIntegerField(default=0)