from django.db import models
from django.utils import timezone

class Registration(models.Model):
    Email = models.CharField(max_length=20)
    subject = models.CharField(max_length=20,null=True)
    text = models.CharField(max_length=400)

    def __str__(self):
        return self.Email

class UserLists(models.Model):
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    Email = models.EmailField(max_length=20)

    def __str__(self):
        return self.name
