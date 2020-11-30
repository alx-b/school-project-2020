# from django.urls import reverse
# from django.contrib.auth.models import User as auth_user
#
# from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
#
#
# import pytest
#
# from tags.views import TagCreate
# from posts.models import Post
# from tags.models import Tag
# from accounts.forms import RegisterForm
#
#
## TESTS --------------------------------------------------------------
# @pytest.mark.parametrize(
#    "username, pass1, pass2, result",
#    [
#        ("hello3", "!#¤%1345", "!#¤%1345", True),
#        # bad password
#        ("hello4", "¤%1345", "¤%1345", False),
#        # bad name
#        ("hel lo3", "!#¤%1345", "!#¤%1345", False),
#        # not maching password
#        ("hello5", "!#¤%134512", "!#¤%134500", False),
#        # all numerics not allowed
#        ("hello6", "1234567890", "1234567890", False),
#        # too common
#        ("hello7", "qwerty123", "qwerty123", False),
#        # Existing user
#        ("testuser1", "!#¤%1345", "!#¤%1345", False),
#    ],
# )
# @pytest.mark.django_db
# def test_visitor_can_register(username, pass1, pass2, result):
#    form = RegisterForm(
#        data={"username": username, "password1": pass1, "password2": pass2}
#    )
#    assert form.is_valid() is result
#
#
# @pytest.mark.parametrize(
#    "username, pass1, result",
#    [
#        ("testuser1", "!#¤%1345", True),
#        ("testuser2", "!#¤%1345", True),
#        # user dont exist
#        ("testuser4", "!#¤%1345", False),
#        # wrong password
#        ("testuser2", "!#¤%12345", False),
#    ],
# )
# @pytest.mark.django_db
# def test_user_can_log_in(username, pass1, result):
#    form = AuthenticationForm(data={"username": username, "password": pass1})
#    assert form.is_valid() is result
#
#
# @pytest.mark.parametrize(
#    "oldpass, pass1, pass2, result",
#    [
#        ("!#¤%1345", "!#¤%1345", "!#¤%1345", True),
#        # Wrong old password
#        ("!#¤%1234", "!#¤%13456", "!#¤%13456", False),
#        # Non-secure new password
#        ("!#¤%1345", "1234567890", "1234567890", False),
#    ],
# )
# @pytest.mark.django_db
# def test_change_password(client, django_user_model, oldpass, pass1, pass2, result):
#    user = django_user_model.objects.get(id=1)
#    client.force_login(user)
#
#    form = PasswordChangeForm(
#        user,
#        data={
#            "old_password": oldpass,
#            "new_password1": pass1,
#            "new_password2": pass2,
#        },
#    )
#
#    assert form.is_valid() is result
#
#
# @pytest.mark.django_db
# def test_create_tag(client, django_user_model):
#    user = django_user_model.objects.get(id=1)
#    client.force_login(user)
#    view = TagCreate()
#    form = view.super().form
#    view.form_valid(form(user, data={"name": "hello123", "description": "hihihi"}))
#    assert view.form_valid() is True
