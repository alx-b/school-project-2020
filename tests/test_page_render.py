from django.urls import reverse
from django.contrib.auth.models import User as auth_user
import pytest

from posts.models import Post
from tags.models import Tag

# FIXTURES -------------------------------------------------------
@pytest.fixture(scope="module")
def django_db_setup(django_db_setup, django_db_blocker):
    print("setup")
    with django_db_blocker.unblock():
        auth_user.objects.create_user(username="testuser1", password="!#¤%1345")
        Post.objects.create(
            title="title1",
            link="https://google.com",
            text="bleh",
            user_id=auth_user.objects.get(id=1).id,
        )
        Tag.objects.create(name="Music", text="it's a test!")


@pytest.fixture(
    params=["accounts:login", "accounts:register", "posts:posts", "tags:tags"]
)
def page(request):
    return request.param


@pytest.fixture(
    params=[
        "accounts:logout",
        "accounts:profile",
        "posts:post-create",
        "tags:tag-create",
    ]
)
def page_auth(request):
    return request.param


@pytest.fixture(params=["posts:post-update", "posts:post-delete"])
def page_auth_permission(request):
    return request.param


@pytest.mark.django_db
def test_page_render(client, page):
    url = reverse(f"{page}")
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_page_auth_redirect_and_render(client, page_auth):
    url = reverse(f"{page_auth}")
    response = client.get(url, follow=True)
    assert response.status_code == 200


@pytest.mark.django_db
def test_page_auth_render_with_auth_user(client, page_auth, django_user_model):
    user = django_user_model.objects.get(id=1)
    client.force_login(user)
    response = client.get(reverse(f"{page_auth}"))
    assert response.status_code == 200


@pytest.mark.django_db
def test_post_page_render(client):
    post = Post.objects.get(id=1)
    url = reverse("posts:post", kwargs={"pk": post.id})
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_tag_page_render(client):
    tag = Tag.objects.get(id=1)
    url = reverse("tags:tag", kwargs={"name": tag.name})
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_page_auth_permission_render_with_right_auth_user(
    client, page_auth_permission, django_user_model
):
    user = django_user_model.objects.get(id=1)
    post = Post.objects.get(id=1)
    client.force_login(user)
    url = reverse(f"{page_auth_permission}", kwargs={"pk": post.id})
    response = client.get(url)
    assert response.status_code == 200


# Want to modify this one
@pytest.mark.django_db
@pytest.mark.parametrize("page", ["tag-update", "tag-delete"])
def test_pages_render_with_auth_user(client, page, django_user_model):
    user = django_user_model.objects.get(id=1)
    tag = Tag.objects.get(id=1)
    client.force_login(user)
    url = reverse(f"tags:{page}", kwargs={"name": tag.name})
    response = client.get(url)
    assert response.status_code == 200
