from django.urls import path

from . import views

urlpatterns = [
    path('v1/tasks/', views.tasks, name='tasks'),
]