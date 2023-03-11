from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.ProjectList.as_view(), name="project.list"),
    path("<slug:slug>/", views.ProjectDetail.as_view(), name="project.detail"),
]
