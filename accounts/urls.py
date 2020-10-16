from django.urls import path

from .views import RegisterView, ProfileView, LogoutView, LoginView

app_name = "accounts"

urlpatterns = [
    path("", LoginView.as_view(), name="login",),
    path("login/", LoginView.as_view(), name="login",),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", RegisterView.as_view(), name="register"),
    path("profile/", ProfileView.as_view(), name="profile"),
]
