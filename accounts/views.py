from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth import models as auth_models
from django.contrib.auth import views as auth_views
from django.shortcuts import get_object_or_404

from .forms import RegisterForm
from tags.models import Tag
from posts.models import Post

# Create your views here.
class RegisterView(CreateView):
    form_class = RegisterForm
    success_url = reverse_lazy("accounts:login")
    template_name = "accounts/register.html"


class ProfileView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = auth_models.User
    template_name = "accounts/profile.html"

    def test_func(self):
        user = get_object_or_404(self.model)
        if self.request.user == user:
            return True
        return False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = get_object_or_404(self.model)
        context["followed_tags"] = Tag.objects.filter(followers__id=user.id)
        tags_name = [tag.name for tag in context["followed_tags"]]
        context["posts"] = Post.objects.filter(tags__name__in=tags_name)
        context["user"] = user
        return context


class LoginView(auth_views.LoginView):
    model = auth_models.User
    template_name = "accounts/login.html"


class LogoutView(LoginRequiredMixin, UserPassesTestMixin, auth_views.LogoutView):
    model = auth_models.User
    template_name = "accounts/logout.html"

    def test_func(self):
        user = get_object_or_404(self.model)
        if self.request.user == user:
            return True
        return False
