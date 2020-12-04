from django.urls import path
from .views import ReplyList, ReplyDetail, ReplyUpdate, ReplyDelete

app_name = "replies"

urlpatterns = [
    path("", ReplyList.as_view(), name="replies"),
    path("<int:pk>/", ReplyDetail.as_view(), name="reply"),
    path("<int:pk>/update/", ReplyUpdate.as_view(), name="update"),
    path("<int:pk>/delete/", ReplyDelete.as_view(), name="delete"),
]
