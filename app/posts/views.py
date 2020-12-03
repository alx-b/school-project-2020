from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator

from .models import Post
from tags.models import Tag
from comments.models import Comment
from .forms import TagSelectForm

# Create your views here.


@login_required
def mod_add_tag_to_post(request, **kwargs):
    mod_tags = Tag.objects.filter(moderators=request.user.id)
    post = get_object_or_404(Post, id=kwargs["pk"])
    choices = [(tag.name, tag.name) for tag in mod_tags]
    if request.method == "POST":
        form = TagSelectForm(choices, request.POST)
        if form.is_valid():
            tag_names = form.cleaned_data["names"]
            query = Tag.objects.filter(name__in=tag_names)
            for tag in query:
                post.tags.add(tag)
            return redirect("posts:post", pk=post.id)
        messages.error(request, "Form is not valid.")
        return render(request, "posts/moderator_tag_add.html", {"form": form})
    form = TagSelectForm(choices)
    return render(request, "posts/moderator_tag_add.html", {"form": form})


@login_required
def mod_remove_tag_from_post(request, **kwargs):
    mod_tags = Tag.objects.filter(moderators=request.user.id)
    post = get_object_or_404(Post, id=kwargs["pk"])
    choices = [(tag.name, tag.name) for tag in mod_tags]
    if request.method == "POST":
        form = TagSelectForm(choices, request.POST)
        if form.is_valid():
            tag_names = form.cleaned_data["names"]
            query = Tag.objects.filter(name__in=tag_names)
            for tag in query:
                post.tags.remove(tag)
            return redirect("posts:post", pk=post.id)
        messages.error(request, "Form is not valid.")
        return render(request, "posts/moderator_tag_remove.html", {"form": form})
    form = TagSelectForm(choices)
    return render(request, "posts/moderator_tag_remove.html", {"form": form})


class PostList(ListView):
    model = Post
    template_name = "posts/posts.html"
    paginate_by = 16
    ordering = ["-date_posted"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class PostDetail(DetailView):
    model = Post
    template_name = "posts/post.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context["moderator"] = Tag.objects.filter(moderators=self.request.user)
        comments = Comment.objects.filter(post=self.kwargs["pk"]).order_by(
            "-date_posted"
        )

        paginator = Paginator(comments, 16)
        page_number = self.request.GET.get("page")
        context["page_object"] = paginator.get_page(page_number)

        comments = Comment.objects.filter(post=self.kwargs["pk"])
        total_replies = 0
        for comment in comments:
            total_replies += comment.reply_set.count()

        context["total_replies"] = total_replies

        return context


class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    fields = ["title", "link", "text", "tags"]
    template_name = "posts/post_create.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PostUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ["title", "link", "text", "tags"]
    template_name = "posts/post_update.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        return False


class PostDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "posts/post_delete.html"
    success_url = reverse_lazy("posts:posts")

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        return False
