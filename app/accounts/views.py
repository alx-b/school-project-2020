from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic import CreateView, DeleteView, UpdateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth import models as auth_models
from django.contrib.auth import views as auth_views
from django.shortcuts import get_object_or_404
from django.db.models import Count
from django.core.paginator import Paginator
from django.contrib.messages.views import SuccessMessageMixin

from .forms import RegisterForm, UserChangeForm
from tags.models import Tag
from posts.models import Post

# Create your views here.
class RegisterView(SuccessMessageMixin, CreateView):
    form_class = RegisterForm
    success_url = reverse_lazy("accounts:login")
    template_name = "accounts/register.html"
    success_message = "Account '%(username)s' was created successfully!"


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
        context["followed_tags"] = Tag.objects.filter(followers__id=user.id).order_by(
            "name"
        )
        context["moderated_tags"] = Tag.objects.filter(moderators__id=user.id).order_by(
            "name"
        )
        tags_name = [tag.name for tag in context["followed_tags"]]
        posts = (
            Post.objects.filter(tags__name__in=tags_name)
            .annotate(Count("id"))
            .order_by("-date_posted")
        )

        paginator = Paginator(posts, 16)
        page_number = self.request.GET.get("page")
        context["page_object"] = paginator.get_page(page_number)
        context["user"] = user
        return context


class PasswordUpdateView(SuccessMessageMixin, auth_views.PasswordChangeView):
    model = auth_models.User
    template_name = "accounts/update.html"
    success_url = reverse_lazy("accounts:profile")
    success_message = "Password was successfully changed!"


class UsernameUpdateView(
    SuccessMessageMixin, LoginRequiredMixin, UserPassesTestMixin, UpdateView
):
    model = auth_models.User
    fields = ["username"]
    template_name = "accounts/username_update.html"
    success_url = reverse_lazy("accounts:profile")
    success_message = "Username was successfully changed!"

    def test_func(self):
        if (
            self.request.user.is_authenticated
            and self.request.user.id == self.kwargs["pk"]
        ):
            return True
        return False
