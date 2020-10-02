from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    link = models.URLField(max_length=300)
    text = models.TextField(max_length=3000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # tags =
    date_posted = models.DateTimeField(default=timezone.now)
    last_updated = models.DateTimeField(null=True)

    def get_absolute_url(self):
        return reverse("posts:post", kwargs={"pk": self.pk})
