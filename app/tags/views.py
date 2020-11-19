from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth import models as auth_models
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Count

from .models import Tag
from .forms import ModeratorForm
from posts.models import Post

# Create your views here.


class TagList(ListView):
    model = Tag
    template_name = "tags/tags.html"
    ordering = ["name"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class TagListOrderByFollowers(ListView):
    model = Tag
    template_name = "tags/tags.html"
    # ordering = ["-followers"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self):
        query = Tag.objects.annotate(Count("followers__id")).order_by(
            "-followers__id__count"
        )
        return query


class TagListOrderByPosts(ListView):
    model = Tag
    template_name = "tags/tags.html"
    # ordering = ["-followers"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self):
        query = Tag.objects.annotate(Count("post__id")).order_by("-post__id__count")
        return query


class TagDetail(DetailView):
    model = Tag
    template_name = "tags/tag.html"
    # queryset = Post.objects.filter(tags__name=Tag.name)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        posts = Post.objects.filter(tags__name=self.kwargs["name"]).order_by(
            "-date_posted"
        )
        paginator = Paginator(posts, 16)
        page_number = self.request.GET.get("page")
        page_object = paginator.get_page(page_number)
        context.update({"page_object": page_object})
        return context

    def get_object(self):
        object = get_object_or_404(Tag, name=self.kwargs["name"])
        return object


@login_required
def add_user_to_followers(request, name, **kwargs):
    user = request.user
    tag = get_object_or_404(Tag, name=name)
    if request.method == "POST":
        tag.followers.add(user)
        return redirect("tags:tag", name=tag.name)
    return redirect("tags:tag", name=tag.name)


@login_required
def remove_user_from_followers(request, name, **kwargs):
    user = request.user
    tag = get_object_or_404(Tag, name=name)
    if request.method == "POST":
        tag.followers.remove(user)
        return redirect("tags:tag", name=tag.name)
    return redirect("tags:tag", name=tag.name)


@login_required
def add_user_to_moderators(request, name, **kwargs):
    tag = get_object_or_404(Tag, name=name)
    if request.user in tag.moderators.all():
        if request.method == "POST":
            form = ModeratorForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data["username"]
                try:
                    user = auth_models.User.objects.get(username=username)
                    tag.moderators.add(user)
                except Exception:
                    messages.error(request, "User doesn't exist.")
                finally:
                    return redirect("tags:tag", name=tag.name)
        form = ModeratorForm()
        return render(request, "tags/moderator_create.html", {"form": form})
    else:
        return redirect("tags:tag", name=tag.name)


@login_required
def remove_user_from_moderators(request, name, **kwargs):
    tag = get_object_or_404(Tag, name=name)
    if request.user in tag.moderators.all():
        if request.method == "POST":
            form = ModeratorForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data["username"]
                try:
                    user = auth_models.User.objects.get(username=username)
                    tag.moderators.remove(user)
                except Exception:
                    messages.error(request, "User doesn't exist.")
                finally:
                    return redirect("tags:tag", name=tag.name)
        form = ModeratorForm()
        return render(request, "tags/moderator_delete.html", {"form": form})
    else:
        return redirect("tags:tag", name=tag.name)


class TagCreate(LoginRequiredMixin, CreateView):
    model = Tag
    fields = ["name", "text", "moderators"]
    template_name = "tags/tag_create.html"

    def form_valid(self, form):
        return super().form_valid(form)


class TagUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Tag
    fields = ["name", "text"]
    template_name = "tags/tag_update.html"

    def form_valid(self, form):
        # form.instance.user = self.request.user
        return super().form_valid(form)

    def get_object(self):
        object = get_object_or_404(Tag, name=self.kwargs["name"])
        return object

    def test_func(self):
        tag = self.get_object()
        if self.request.user in tag.moderators.all():
            return True
        return False


class TagDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Tag
    template_name = "tags/tag_delete.html"
    success_url = reverse_lazy("tags:tags")

    def get_object(self):
        object = get_object_or_404(Tag, name=self.kwargs["name"])
        return object

    def test_func(self):
        tag = self.get_object()
        if self.request.user in tag.moderators.all():
            return True
        return False
