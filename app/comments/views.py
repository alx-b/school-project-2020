from django.shortcuts import render

from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Comment
from posts.models import Post

# Create your views here.


class CommentList(ListView):
    model = Comment
    template_name = "comments/comments.html"
    paginate_by = 16
    ordering = ["-date_posted"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CommentDetail(DetailView):
    model = Comment
    template_name = "comments/comment.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # if self.request.user.is_authenticated:
        #    context["moderator"] = Tag.objects.filter(moderators=self.request.user)
        return context


class CommentCreate(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ["text"]
    template_name = "comments/comment_create.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context["post"] = Post.objects.get(pk=self.kwargs["pk"])
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.post = Post.objects.get(pk=self.kwargs["pk"])
        return super().form_valid(form)


class CommentUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    fields = ["text"]
    template_name = "comments/comment_update.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        comment = self.get_object()
        if self.request.user == comment.user:
            return True
        return False


class CommentDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = "comments/comment_delete.html"
    success_url = reverse_lazy("comments:comments")

    def test_func(self):
        comment = self.get_object()
        if self.request.user == comment.user:
            return True
        return False
