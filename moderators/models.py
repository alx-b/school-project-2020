from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from tags.models import Tag

# Create your models here.
class Moderator(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    tag_id = models.ForeignKey(Tag, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("moderators:moderator", kwargs={"name": self.user_id.username})

    def __str__(self):
        return self.user_id.username
