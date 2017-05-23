from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User)

    # add additional info
    profile_site = models.URLField(blank=True)
    profile_pics = models.ImageField(upload_to="profile_pics", blank=True)
    createdDate = models.DateTimeField(auto_created=True, auto_now=True)

    def __str__(self):
        return self.user.username
