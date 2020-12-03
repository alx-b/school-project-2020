from django.urls import path
from .views import CommentList, CommentDetail, CommentDelete, CommentUpdate

from replies.views import ReplyCreate

app_name = "comments"

urlpatterns = [
    path("", CommentList.as_view(), name="comments"),
    path("<int:pk>/", CommentDetail.as_view(), name="comment"),
    path("<int:pk>/update/", CommentUpdate.as_view(), name="comment-update"),
    path("<int:pk>/delete/", CommentDelete.as_view(), name="comment-delete"),
    path("<int:pk>/reply-create/", ReplyCreate.as_view(), name="comment-reply-create"),
]
