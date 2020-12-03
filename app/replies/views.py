from django.shortcuts import render

from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.

from .models import Reply
from comments.models import Comment


class ReplyList(ListView):
    model = Reply
    template_name = "replies/replies.html"
    paginate_by = 16
    ordering = ["-date_posted"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ReplyDetail(DetailView):
    model = Reply
    template_name = "replies/reply.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ReplyCreate(LoginRequiredMixin, CreateView):
    model = Reply
    fields = ["text"]
    template_name = "replies/reply_create.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context["comment"] = Comment.objects.get(pk=self.kwargs["pk"])
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.comment = Comment.objects.get(pk=self.kwargs["pk"])
        return super().form_valid(form)
