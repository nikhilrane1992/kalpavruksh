from django.db import models

class User(models.Model):
    name = models.CharField(max_length=50)

class Question(models.Model):
    title = models.TextField()
    user = models.OneToOneField(User)
    private = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
   
class Question(models.Model):
    body = models.TextField()
    user = models.OneToOneField(User)
    question = models.ForeignKey(Question)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

class Tenant(models.Model):
    name = models.CharField(max_length=50)
    api_key = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
   