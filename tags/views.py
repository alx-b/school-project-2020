from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Tag
from posts.models import Post
from django.contrib.auth import models as auth_models

# Create your views here.


class TagList(ListView):
    model = Tag
    template_name = "tags/tags.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class TagDetail(DetailView):
    model = Tag
    template_name = "tags/tag.html"
    # queryset = Post.objects.filter(tags__name=Tag.name)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        some_data = Post.objects.filter(tags__name=self.kwargs["name"])
        context.update({"some_data": some_data})
        return context

    def get_object(self):
        object = get_object_or_404(Tag, name=self.kwargs["name"])
        return object


def add_user_to_followers(request, name, **kwargs):
    user = get_object_or_404(auth_models.User)
    tag = get_object_or_404(Tag, name=name)
    if request.method == "POST":
        tag.followers.add(user)
        return redirect("tags:tag", name=tag.name)
    return redirect("tags:tag", name=tag.name)


def remove_user_from_followers(request, name, **kwargs):
    user = get_object_or_404(auth_models.User)
    tag = get_object_or_404(Tag, name=name)
    if request.method == "POST":
        tag.followers.remove(user)
        return redirect("tags:tag", name=tag.name)
    return redirect("tags:tag", name=tag.name)


class TagCreate(LoginRequiredMixin, CreateView):
    model = Tag
    fields = ["name", "text"]
    template_name = "tags/tag_create.html"

    def form_valid(self, form):
        # form.instance.user = self.request.user
        return super().form_valid(form)


class TagUpdate(LoginRequiredMixin, UpdateView):
    model = Tag
    fields = ["name", "text"]
    template_name = "tags/tag_update.html"

    def form_valid(self, form):
        # form.instance.user = self.request.user
        return super().form_valid(form)

    def get_object(self):
        object = get_object_or_404(Tag, name=self.kwargs["name"])
        return object

    # def test_func(self):
    #    post = self.get_object()
    #    if self.request.user == post.user:
    #        return True
    #    return False
    #


class TagDelete(LoginRequiredMixin, DeleteView):
    model = Tag
    template_name = "tags/tag_delete.html"
    success_url = reverse_lazy("tags:tags")

    def get_object(self):
        object = get_object_or_404(Tag, name=self.kwargs["name"])
        return object

    # def test_func(self):
    #    post = self.get_object()
    #    if self.request.user == post.user:
    #        return True
    #    return False
