from django.contrib.auth.models import User as auth_user

from posts.models import Post
from tags.models import Tag

import pytest


@pytest.fixture(scope="session")
def django_db_setup(django_db_setup, django_db_blocker):
    print("setup")
    with django_db_blocker.unblock():
        auth_user.objects.create_user(username="testuser1", password="!#¤%1345")
        auth_user.objects.create_user(username="testuser2", password="!#¤%1345")
        Post.objects.create(
            title="title1",
            link="https://google.com",
            text="bleh",
            user_id=auth_user.objects.get(id=1).id,
        )
        Post.objects.create(
            title="title2",
            link="https://google.com",
            text="bleh2",
            user_id=auth_user.objects.get(id=2).id,
        )
        Tag.objects.create(name="Music", text="it's a test!")
