from django.urls import path

from .views import TagList, TagDetail, TagCreate, TagDelete, TagUpdate

app_name = "tags"

urlpatterns = [
    path("", TagList.as_view(), name="tags"),
    path("create/", TagCreate.as_view(), name="tag-create"),
    path("<slug:name>/", TagDetail.as_view(), name="tag"),
    path("<slug:name>/update/", TagUpdate.as_view(), name="tag-update"),
    path("<slug:name>/delete/", TagDelete.as_view(), name="tag-delete"),
]
