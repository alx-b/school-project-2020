from django.db import models
from django.urls import reverse

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=100)
    text = models.CharField(max_length=3000)

    def get_absolute_url(self):
        return reverse("tags:tag", kwargs={"name": self.name})

    def __str__(self):
        return self.name
