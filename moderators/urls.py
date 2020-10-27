from django.urls import path
from .views import ModeratorList, ModeratorCreate

app_name = "moderators"

urlpatterns = [
    path("", ModeratorList.as_view(), name="moderators"),
    path("create/", ModeratorCreate.as_view(), name="moderator-create"),
]
