from django.urls import path

from .views import (
    TagList,
    TagDetail,
    TagCreate,
    TagDelete,
    TagUpdate,
    add_user_to_followers,
    remove_user_from_followers,
    add_user_to_moderators,
    remove_user_from_moderators,
    TagListOrderByFollowers,
    TagListOrderByPosts,
)

app_name = "tags"

urlpatterns = [
    path("", TagList.as_view(), name="tags"),
    path(
        "order_by_followers/",
        TagListOrderByFollowers.as_view(),
        name="tags-order-followers",
    ),
    path("order_by_posts/", TagListOrderByPosts.as_view(), name="tags-order-posts"),
    path("create/", TagCreate.as_view(), name="tag-create"),
    path("add_follower/<slug:name>", add_user_to_followers, name="add-follower"),
    path(
        "remove_follower/<slug:name>",
        remove_user_from_followers,
        name="remove-follower",
    ),
    path("<slug:name>/", TagDetail.as_view(), name="tag"),
    path("<slug:name>/update/", TagUpdate.as_view(), name="tag-update"),
    path("<slug:name>/delete/", TagDelete.as_view(), name="tag-delete"),
    path(
        "<slug:name>/add_moderator/",
        add_user_to_moderators,
        name="add-moderator",
    ),
    path(
        "<slug:name>/remove_moderator/",
        remove_user_from_moderators,
        name="remove-moderator",
    ),
]
