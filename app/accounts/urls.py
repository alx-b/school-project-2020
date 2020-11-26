from django.urls import path
from django.contrib.auth import views as auth_views

from .views import RegisterView, ProfileView, PasswordUpdateView

app_name = "accounts"

urlpatterns = [
    path(
        "",
        auth_views.LoginView.as_view(template_name="accounts/login.html"),
        name="login",
    ),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="accounts/login.html"),
        name="login",
    ),
    path("pass-update/", PasswordUpdateView.as_view(), name="update"),
    path(
        "logout/",
        auth_views.LogoutView.as_view(template_name="accounts/logout.html"),
        name="logout",
    ),
    path("register/", RegisterView.as_view(), name="register"),
    path("profile/", ProfileView.as_view(), name="profile"),
]
