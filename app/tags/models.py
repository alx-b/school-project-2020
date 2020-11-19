from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.template.defaultfilters import slugify

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=100)
    text = models.CharField(max_length=3000)
    followers = models.ManyToManyField(User, related_name="user_follower")
    moderators = models.ManyToManyField(User, related_name="user_moderator")

    def get_absolute_url(self):
        return reverse("tags:tag", kwargs={"name": self.name})

    def save(self, *args, **kwargs):
        if not self.id:
            # Newly created object, so set slug
            self.name = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
