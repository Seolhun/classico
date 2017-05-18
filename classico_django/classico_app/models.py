from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):
    id = models.BigAutoField(primary_key=True)
    topic_name = models.CharField(max_length=255, unique=True)
    createdBy = models.ForeignKey(User)
    createdDate = models.DateTimeField(auto_created=True, auto_now=True)
    
    def __str__(self):
        return self.topic_name


class WebPage(models.Model):
    id = models.BigAutoField(primary_key=True)
    topic = models.ForeignKey(Topic)
    name = models.CharField(max_length= 255, unique=True)
    url = models.URLField(unique=True)
    
    def __str__(self):
        return self.name


class AccessRecord(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.ForeignKey(WebPage)
    createdDate = models.DateTimeField(auto_created=True, auto_now=True)

    def __str__(self):
        return self.createdDate


class Board(models.Model):
    id = models.BigAutoField(primary_key=True)
    subject = models.CharField(max_length=200)
    content = models.TextField(max_length=255)
    hits = models.IntegerField()
    createdBy = models.ForeignKey(User)
    createdDate = models.DateTimeField(auto_created=True, auto_now=True)

    def __str__(self):
        return self.subject
