from django.db import models
from accounts.models import User
from django.conf import settings
# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)