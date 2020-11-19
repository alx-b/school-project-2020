from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User

from tags.models import Tag

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    link = models.URLField(max_length=300, null=True, blank=True)
    text = models.TextField(max_length=3000, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    last_updated = models.DateTimeField(null=True)

    def get_absolute_url(self):
        return reverse("posts:post", kwargs={"pk": self.pk})

    def __str__(self):
        return self.title
