from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth import models as auth_models
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
        if self.request.user.is_authenticated:
            return True
        return False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context["followed_tags"] = Tag.objects.filter(followers__id=user.id)
        tags_name = [tag.name for tag in context["followed_tags"]]
        context["posts"] = Post.objects.filter(tags__name__in=tags_name)
        context["user"] = user
        return context
