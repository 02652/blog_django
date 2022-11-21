from django.db import models
from taggit.managers import TaggableManager
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Author(AbstractUser):
    name = models.CharField(max_length=50)
    account_twitter = models.CharField(max_length=30)
    description = models.TextField()
    street = models.CharField(null=True, blank=True, max_length=30)
    number = models.CharField(null=True, blank=True, max_length=20)
    door = models.CharField(null=True, blank=True, max_length=10)
    postal_code = models.CharField(null=True, blank=True, max_length=20)
    city = models.CharField(null=True, blank=True, max_length=20)
    number_phone = models.CharField(null=True, blank=True, max_length=20)

    def __str__(self):
        return self.name

class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    publication_date = models.DateTimeField(auto_now_add=True)
    tags = TaggableManager()

    def __str__(self):
        return self.title + '-' + self.author.username

class Comment(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    publication_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content

#
# class PhoneNumber(models.Model):
#     author = models.ForeignKey(Author, on_delete=models.CASCADE)
#     number_phone = models.CharField(max_length=20)
