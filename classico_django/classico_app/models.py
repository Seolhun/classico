from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class UserProfile(models.Model):
    user = models.OneToOneField(User)

    # add additional info
    profile_site = models.URLField(blank=True)
    profile_pics = models.ImageField(upload_to="profile_pics", blank=True)
    createdDate = models.DateTimeField(default=timezone.now)
    modifiedBy = models.CharField(max_length=200, null=True)
    modifiedDate = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.modifiedDate = timezone.now
        self.save()

    def __str__(self):
        return self.user.username
