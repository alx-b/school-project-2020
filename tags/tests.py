from django.test import TestCase

"""
from django.urls import reverse
from .models import Tag
import pytest


# Create your tests here.


@pytest.fixture
def auth_user(django_user_model):
    auth_user = django_user_model.objects.create_user(
        username="testuser1", password="!#¤%1345"
    )
    return auth_user


@pytest.fixture
def tag():
    tag = Tag(name="Music", text="it's a test!")
    tag.save()
    return tag


@pytest.mark.django_db
def test_render_tags_page(client):
    url = reverse("tags:tags")
    response = client.get(url)
    print(response.content)
    assert response.status_code == 200


@pytest.mark.django_db
def test_render_tag_page(client, tag):
    url = reverse("tags:tag", kwargs={"name": tag.name})
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.parametrize("page", ["tag-create"])
def test_page_redirect_and_render(client, page):
    url = reverse(f"tags:{page}")
    response = client.get(url, follow=True)
    assert response.status_code == 200


@pytest.mark.parametrize("page", ["tag-create"])
def test_page_render_with_auth_user(client, page, auth_user):
    client.force_login(auth_user)
    url = reverse(f"tags:{page}")
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
@pytest.mark.parametrize("page", ["tag-update", "tag-delete"])
def test_pages_render_with_auth_user(client, page, auth_user, tag):
    client.force_login(auth_user)
    url = reverse(f"tags:{page}", kwargs={"name": tag.name})
    response = client.get(url)
    assert response.status_code == 200
"""
