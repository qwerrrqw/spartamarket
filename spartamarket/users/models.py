from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.

class profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    image = models.ImageField(default="users/user.png", upload_to="images/")
    created_at = models.DateTimeField(default=timezone.now)