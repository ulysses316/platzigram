from django.db import models

# Create your models here.

class User(models.Model):
    email = models.EmailField(unique = True)
    password = models.CharField(max_length = 16)
    is_admin = models.BooleanField(default=False)

    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 20)

    bio = models.TextField(blank=True)
    birthday = models.DateField(blank = True, null = True)

    created = models.DateTimeField(auto_now_add = True)
    modified = models.DateTimeField(auto_now=True)
