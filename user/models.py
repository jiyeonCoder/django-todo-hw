from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    profile = models.TextField(null=True, blank=True)
    like_todos = models.ManyToManyField('todo.Todo', related_name='like_users')
    follow = models.ManyToManyField(
        'self', symmetrical=False, related_name='followers')
