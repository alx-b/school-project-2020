from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import models as auth_models


class RegisterForm(UserCreationForm):
    class Meta:
        fields = ("username", "password1", "password2")
        model = auth_models.User

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
