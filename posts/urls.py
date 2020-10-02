from django.urls import path
from .views import PostList, PostDetail, PostCreate, PostDelete, PostUpdate

app_name = "posts"

urlpatterns = [
    path("", PostList.as_view(), name="posts"),
    path("create/", PostCreate.as_view(), name="post-create"),
    path("<int:pk>/", PostDetail.as_view(), name="post"),
    path("<int:pk>/update/", PostUpdate.as_view(), name="post-update"),
    path("<int:pk>/delete/", PostDelete.as_view(), name="post-delete"),
]
