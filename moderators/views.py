from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from tags.models import Tag
from posts.models import Post
from django.contrib.auth import models as auth_models

from .models import Moderator


# Create your views here.
#
#
class ModeratorList(ListView):
    model = Moderator
    template_name = "moderators/moderators.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ModeratorCreate(LoginRequiredMixin, CreateView):
    model = Moderator
    fields = ["user_id"]
    template_name = "moderators/moderator_create.html"

    def form_valid(self, form):
        # form.instance.user = self.request.user
        user = auth_models.User.objects.filter(user__username=self.kwargs["username"])
        if user:
            return super().form_valid(form)
