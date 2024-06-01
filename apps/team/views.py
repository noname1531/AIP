from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView

from .models import *
from .serializers import *

class TeamAPIViwe(ListAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class TeamAPICreate(CreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class TeamAPIRetrieve(RetrieveAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamDetailSerializer

class TeamAPIDestroy(DestroyAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamDestroySerializer

class TeamAPIUpdate(UpdateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamUpdateSerializer
