from django import forms
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views import generic, View

from app.models import Task, Tag


class HomeView(generic.ListView):
    model = Task
    template_name = "app/index.html"
    context_object_name = "tasks"

    def get_queryset(self):
        return Task.objects.order_by("done", "-datetime")


class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    template_name = "app/task_form.html"
    success_url = reverse_lazy("app:home")

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        form.fields["deadline"].widget = forms.DateInput(
            attrs={"type": "date", "class": "form-control"}
        )
        return form


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    template_name = "app/task_form.html"
    success_url = reverse_lazy("app:home")

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        form.fields["deadline"].widget = forms.DateInput(
            attrs={"type": "date", "class": "form-control"}
        )
        return form


class TaskDeleteView(generic.DeleteView):
    model = Task
    template_name = "app/task_delete.html"
    success_url = reverse_lazy("app:home")


class TaskToggleView(View):
    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.done = not task.done
        task.save(update_fields=["done"])
        next_url = request.POST.get("next") or request.META.get("HTTP_REFERER")
        return redirect(next_url or reverse("app:home"))


class TagListView(generic.ListView):
    model = Tag
    template_name = "app/tag_list.html"
    context_object_name = "tags"


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    template_name = "app/tag_form.html"
    success_url = reverse_lazy("app:tag-list")


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    template_name = "app/tag_form.html"
    success_url = reverse_lazy("app:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    template_name = "app/tag_delete.html"
    success_url = reverse_lazy("app:tag-list")
