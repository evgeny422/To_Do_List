from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View

from todo.models import Project


# Create your views here.

class ProjectList(View):
    """
    Список проектов пользователя
    """

    def get(self, request, *args, **kwargs):
        projects = Project.objects.prefetch_related('task_project').prefetch_related('tag').all()

        return render(request, 'todo/project/project_list.html', {
            'projects': projects
        })


class ProjectDetail(View):
    """
    Отображение проекта пользователя
    """

    def get(self, request, *args, **kwargs):
        project = get_object_or_404(
            Project.objects.prefetch_related('task_project').prefetch_related('tag'), slug=kwargs.get('slug'))

        return render(request, 'todo/project/project_detail.html', {
            'project': project
        })


def post(self, request, *args, **kwargs):
    pass
