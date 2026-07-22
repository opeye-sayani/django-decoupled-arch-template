from apps.authentication.models import Task

def create_task(*, title: str, description: str = '', completed: bool = False) -> Task:
    task = Task.objects.create(
        title=title,
        description=description,
        completed=completed
    )
    return task

def update_task(*, task_id, **data) -> Task:
    task = Task.objects.get(id=task_id)
    
    # Dynamically update only the fields provided in the payload
    for field, value in data.items():
        setattr(task, field, value)
        
    task.save()
    return task

def delete_task(*, task_id) -> None:
    # Uses filter().delete() to avoid fetching the object into memory first
    Task.objects.filter(id=task_id).delete()