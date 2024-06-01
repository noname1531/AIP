from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView

from .models import *
from .serializers import *

# Create your views here.
class TaskAPIViwe(ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskAPICreate(CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskAPIRetrieve(RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class =TaskDetailSerializer

class TaskAPIDestroy(DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskDestroySerializer

class TaskAPIUpdate(UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskUpdateSerializer
