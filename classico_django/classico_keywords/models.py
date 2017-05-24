from django.db import models
from django.utils import timezone


class stackObject(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=200)
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

    def getAbsoluteUrl(self):
        return reversed("post_detail", kwargs={'pk': self.pk})

    def __str__(self):
        return self.name
