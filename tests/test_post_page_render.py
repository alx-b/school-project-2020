from django.urls import reverse
from django.contrib.auth.models import User as auth_user

import pytest

from posts.models import Post
from tags.models import Tag
from accounts.forms import RegisterForm

# FIXTURES -------------------------------------------------------


# TESTS --------------------------------------------------------------
# @pytest.mark.parametrize(
#    "page, expected_status_code",
#    [
#        ("accounts:register", 200),
#        ("accounts:login", 200),
#        # By default logout is also accessible to visitor user.
#        ("accounts:logout", 200),
#        ("accounts:profile", 302),
#        ("posts:posts", 200),
#        ("tags:tags", 200),
#        ("posts:post-create", 302),
#        ("tags:tag-create", 302),
#        ("posts:post", 200),
#        ("tags:tag", 200),
#    ],
# )


def test_visitor_can_register(client):
    form = RegisterForm()
    form.username = "hello3"
    form.password1 = "!#¤%1345"
    form.password2 = "!#¤%1345"
    assert form.is_valid()


"""
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
"""
