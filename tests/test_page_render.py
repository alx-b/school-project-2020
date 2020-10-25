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


# TESTS --------------------------------------------------------------
@pytest.mark.parametrize(
    "page, expected_status_code",
    [
        ("accounts:register", 200),
        ("accounts:login", 200),
        # By default logout is also accessible to visitor user.
        ("accounts:logout", 200),
        ("accounts:profile", 302),
        ("posts:posts", 200),
        ("tags:tags", 200),
        ("posts:post-create", 302),
        ("tags:tag-create", 302),
        ("posts:post", 200),
        ("tags:tag", 200),
    ],
)
@pytest.mark.django_db
def test_page_expected_html_status_code_with_visitor(
    client, page, expected_status_code
):
    response = ""
    if page == "posts:post":
        print("hello post")
        post = Post.objects.get(id=1)
        response = client.get(reverse(page, kwargs={"pk": post.id}))
    elif page == "tags:tag":
        print("hello tags")
        tag = Tag.objects.get(id=1)
        response = client.get(reverse(page, kwargs={"name": tag.name}))
    else:
        response = client.get(reverse(page))

    assert response.status_code == expected_status_code


@pytest.mark.parametrize(
    "page, expected_status_code",
    [
        # Default register/login accessible to auth user??
        ("accounts:register", 302),
        ("accounts:login", 302),
        ("accounts:logout", 200),
        ("accounts:profile", 200),
        ("posts:posts", 200),
        ("tags:tags", 200),
        ("posts:post-create", 200),
        ("tags:tag-create", 200),
        ("posts:post", 200),
        ("tags:tag", 200),
    ],
)
@pytest.mark.django_db
def test_page_expected_status_code_with_authenticated_user(
    client, django_user_model, page, expected_status_code
):
    user = django_user_model.objects.get(id=1)
    client.force_login(user)
    response = ""
    if page == "posts:post":
        print("hello post")
        post = Post.objects.get(id=1)
        response = client.get(reverse(page, kwargs={"pk": post.id}))
    elif page == "tags:tag":
        print("hello tags")
        tag = Tag.objects.get(id=1)
        response = client.get(reverse(page, kwargs={"name": tag.name}))
    else:
        response = client.get(reverse(page))

    assert response.status_code == expected_status_code


@pytest.mark.parametrize(
    "page, expected_status_code",
    [
        ("posts:post-update", 302),
        ("posts:post-delete", 302),
    ],
)
@pytest.mark.django_db
def test_visitor_page_expected_status_code(client, page, expected_status_code):
    post = Post.objects.get(id=2)
    response = client.get(reverse(page, kwargs={"pk": post.id}))
    assert response.status_code == expected_status_code


@pytest.mark.parametrize(
    "page, expected_status_code",
    [
        ("posts:post-update", 403),
        ("posts:post-delete", 403),
    ],
)
@pytest.mark.django_db
def test_unauthorized_authenticated_user_page_expected_status_code(
    client, django_user_model, page, expected_status_code
):
    user = django_user_model.objects.get(id=1)
    client.force_login(user)
    post = Post.objects.get(id=2)
    response = client.get(reverse(page, kwargs={"pk": post.id}))
    assert response.status_code == expected_status_code


@pytest.mark.parametrize(
    "page, expected_status_code",
    [
        ("posts:post-update", 200),
        ("posts:post-delete", 200),
    ],
)
@pytest.mark.django_db
def test_authorized_authenticated_user_page_expected_status_code(
    client, django_user_model, page, expected_status_code
):
    user = django_user_model.objects.get(id=1)
    client.force_login(user)
    post = Post.objects.get(id=1)
    response = client.get(reverse(page, kwargs={"pk": post.id}))
    assert response.status_code == expected_status_code


@pytest.mark.parametrize(
    "page, expected_status_code",
    [
        ("tags:tag-update", 302),
        ("tags:tag-delete", 302),
    ],
)
@pytest.mark.django_db
def test_visitor_page_expected_status_code(client, page, expected_status_code):
    tag = Tag.objects.get(id=1)
    response = client.get(reverse(page, kwargs={"name": tag.id}))
    assert response.status_code == expected_status_code
