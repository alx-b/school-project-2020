from django.test import TestCase

"""
from django.urls import reverse

import pytest


# Create your tests here.


@pytest.mark.parametrize("page", ["login", "register"])
def test_render_page(client, page):
    url = reverse(f"accounts:{page}")
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.parametrize("page", ["logout", "profile"])
def test_page_redirect_and_render(client, page):
    url = reverse(f"accounts:{page}")
    response = client.get(url, follow=True)
    assert response.status_code == 200


@pytest.mark.parametrize("page", ["logout", "profile"])
@pytest.mark.parametrize("username, password", [("test_user", "!#¤%1345")])
def test_page_render_with_auth_user(
    client, django_user_model, page, username, password
):
    auth_user = django_user_model.objects.create_user(
        username=username, password=password
    )
    client.force_login(auth_user)
    url = reverse(f"accounts:{page}")
    response = client.get(url)
    assert response.status_code == 200
"""
