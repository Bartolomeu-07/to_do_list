from django.urls import path

from app.views import HomeView, TaskCreateView, TaskUpdateView, TaskDeleteView, TaskToggleView, TagListView, \
    TagUpdateView, TagCreateView, TagDeleteView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
    path("tasks/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("tasks/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path("tasks/<int:pk>/toggle/", TaskToggleView.as_view(), name="task-toggle"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/create", TagCreateView.as_view(), name="tag-create"),
    path("tags/<int:pk>/update", TagUpdateView.as_view(), name="tag-update"),
    path("tags/<int:pk>/delete", TagDeleteView.as_view(), name="tag-delete"),
]

app_name = 'app'