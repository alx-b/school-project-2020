from django.urls import path
from .views import ReplyList, ReplyDetail

app_name = "replies"

urlpatterns = [
    path("", ReplyList.as_view(), name="replies"),
    path("<int:pk>/", ReplyDetail.as_view(), name="reply"),
]
