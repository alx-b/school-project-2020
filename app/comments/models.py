from django.db import models

from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User

from posts.models import Post

# Create your models here.
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=3000, null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    last_updated = models.DateTimeField(null=True)

    def get_absolute_url(self):
        return reverse("comments:comment", kwargs={"pk": self.pk})
