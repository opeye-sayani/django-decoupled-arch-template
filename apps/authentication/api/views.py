from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import TaskSerializer
from .. import services, selectors
from ..models import Task

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    # READ operations route to selectors.py
    def list(self, request, *args, **kwargs):
        tasks = selectors.list_tasks()
        serializer = self.get_serializer(tasks, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        task = selectors.get_task(task_id=kwargs.get('pk'))
        serializer = self.get_serializer(task)
        return Response(serializer.data)

    # WRITE operations route to services.py
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        # Bypassing serializer.save() to use your service layer
        task = services.create_task(**serializer.validated_data)
        
        output_serializer = self.get_serializer(task)
        return Response(output_serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        # Using partial=True to handle both PUT and PATCH
        serializer = self.get_serializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        
        task = services.update_task(task_id=kwargs.get('pk'), **serializer.validated_data)
        
        output_serializer = self.get_serializer(task)
        return Response(output_serializer.data)

    def destroy(self, request, *args, **kwargs):
        services.delete_task(task_id=kwargs.get('pk'))
        return Response(status=status.HTTP_204_NO_CONTENT)