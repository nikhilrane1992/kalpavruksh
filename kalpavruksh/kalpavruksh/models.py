from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    title = models.TextField()
    user = models.ForeignKey(User)
    private = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "{}".format(self.title)
   
class Answer(models.Model):
    body = models.TextField()
    user = models.ForeignKey(User)
    question = models.ForeignKey(Question)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "{}".format(self.body)

class Tenant(models.Model):
    name = models.CharField(max_length=50)
    api_key = models.CharField(max_length=100)
    api_request_count = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "Name: {} | Api Key: {} | Api Request Count: {}".format(self.name, self.api_key, self.api_request_count)
   