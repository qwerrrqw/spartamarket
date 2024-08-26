from django.db import models
from django.conf import settings
from django.utils import timezone


from django.conf import settings
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    image = models.ImageField(default="users/user.png", upload_to="images/")
    created_at = models.DateTimeField(default=timezone.now)

    following = models.ManyToManyField(
        to="self",
        related_name="followers",
        symmetrical=False,
    )