from django.shortcuts import get_object_or_404
from apps.authentication.models import Task

def list_tasks():
    return Task.objects.all()

def get_task(*, task_id):
    # Handles the database lookup and 404 error isolation
    return get_object_or_404(Task, id=task_id)