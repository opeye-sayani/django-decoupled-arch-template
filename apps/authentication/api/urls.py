from django.urls import path
from .views import TaskViewSet
from django.contrib import admin
from rest_framework import routers
from django.urls import include

router = routers.DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')

urlpatterns = [path('' , include(router.urls) )]
