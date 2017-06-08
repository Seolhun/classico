from django.db import models
from django.utils import timezone


class Board(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=200)
    text = models.TextField()
    hits = models.IntegerField(default=0)
    commentDepth = models.IntegerField(default=0)
    fileDepth = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    hates = models.IntegerField(default=0)
    
    createdBy = models.ForeignKey('auth.User')
    createdDate = models.DateTimeField(default=timezone.now)
    modifiedBy = models.CharField(max_length=200, null=True)
    modifiedDate = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.modifiedDate = timezone.now
        self.save()

    def approvedComments(self):
        return self.comments.filter(approvedComments=True)

    def getAbsoluteUrl(self):
        return reversed("post_detail", kwargs={'pk': self.pk })

    def __str__(self):
        return self.title
    
    
class Comment(models.Model):
    id = models.BigAutoField(primary_key=True)
    boardId = models.ForeignKey(Board)
    text = models.TextField()
    approvedComment = models.BooleanField(default=False)
    depth = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    hates = models.IntegerField(default=0)
    
    createdBy = models.ForeignKey('auth.User')
    createdDate = models.DateTimeField(default=timezone.now)
    modifiedBy = models.CharField(max_length=200, null=True)
    modifiedDate = models.DateTimeField(blank=True, null=True)
    
    def publish(self):
        self.modifiedDate = timezone.now
        self.save()

    def approve(self):
        self.approvedComment = True
        self.save()

    def getAbsoluteUrl(self):
        return reversed("post_list", kwargs={ 'pk' : self.pk })

    def __str__(self):
        return self.text


class File(models.Model):
    id = models.BigAutoField(primary_key=True)
    boardId = models.ForeignKey(Board)
    originName = models.CharField(max_length=200)
    savedName = models.CharField(max_length=200)
    size = models.IntegerField(default=0)
    path = models.FilePathField(default=0)
    file = models.FileField(default=0)
    
    createdBy = models.ForeignKey('auth.User')
    createdDate = models.DateTimeField(default=timezone.now)
    modifiedBy = models.CharField(max_length=200, null=True)
    modifiedDate = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.modifiedDate = timezone.now
        self.save()

    def getAbsoluteUrl(self):
        return reversed("post_detail", kwargs={'pk': self.pk })

    def __str__(self):
        return self.originName
