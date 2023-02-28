from django.db import models

# Create your models here.


class Credential(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=50)

    def __str__(self):
          return (self.username)


class Message(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=100)
    url = models.URLField(blank=True, null=True)

    def __str__(self):
          return (self.title)


class Comment(models.Model):
    content = models.CharField(max_length=100)

    def __str__(self):
          return (self.content)