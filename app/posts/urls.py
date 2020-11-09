from django.urls import path
from .views import (
    PostList,
    PostDetail,
    PostCreate,
    PostDelete,
    PostUpdate,
    mod_add_tag_to_post,
    mod_remove_tag_from_post,
)

from comments.views import CommentCreate

app_name = "posts"

urlpatterns = [
    path("", PostList.as_view(), name="posts"),
    path("create/", PostCreate.as_view(), name="post-create"),
    path("<int:pk>/", PostDetail.as_view(), name="post"),
    path("<int:pk>/update/", PostUpdate.as_view(), name="post-update"),
    path("<int:pk>/delete/", PostDelete.as_view(), name="post-delete"),
    path("<int:pk>/mod_tag_add/", mod_add_tag_to_post, name="mod-tag-add"),
    path("<int:pk>/mod_tag_remove/", mod_remove_tag_from_post, name="mod-tag-remove"),
    path(
        "<int:pk>/comment-create/", CommentCreate.as_view(), name="post-comment-create"
    ),
]
