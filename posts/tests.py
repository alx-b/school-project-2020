from django.test import TestCase

"""
from django.urls import reverse
from .models import Post

import pytest


# Create your tests here.
@pytest.fixture
def auth_user(django_user_model):
    auth_user = django_user_model.objects.create_user(
        username="testuser1", password="!#¤%1345"
    )
    return auth_user


@pytest.mark.django_db
@pytest.fixture
def post(auth_user):
    post = Post(
        title="title1", link="https://google.com", text="bleh1", user_id=auth_user.id
    )
    post.save()
    return post


@pytest.mark.django_db
def test_render_posts_page(client):
    url = reverse("posts:posts")
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_render_post_page(client, auth_user, post):
    url = reverse("posts:post", kwargs={"pk": post.id})
    response = client.get(url)
    print(response.content)
    assert response.status_code == 200


@pytest.mark.parametrize("page", ["post-create"])
def test_post_create_page_redirect_and_render(client, page):
    url = reverse(f"posts:{page}")
    response = client.get(url, follow=True)
    assert response.status_code == 200


@pytest.mark.parametrize("page", ["post-create"])
def test_post_create_page_render_with_auth_user(client, page, auth_user):
    client.force_login(auth_user)
    url = reverse(f"posts:{page}")
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
@pytest.mark.parametrize("page", ["post-update", "post-delete"])
def test_pages_render_with_auth_user(client, page, auth_user, post):
    client.force_login(auth_user)
    url = reverse(f"posts:{page}", kwargs={"pk": post.id})
    response = client.get(url)
    assert response.status_code == 200
"""
