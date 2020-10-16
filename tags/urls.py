from django.urls import path

from .views import (
    TagList,
    TagDetail,
    TagCreate,
    TagDelete,
    TagUpdate,
    add_user_to_followers,
    remove_user_from_followers,
)

app_name = "tags"

urlpatterns = [
    path("", TagList.as_view(), name="tags"),
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
]
