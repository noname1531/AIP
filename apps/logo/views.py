from django.shortcuts import render
from rest_framework.generics import ListAPIView

from .models import Logo
from .serializers import LogoSerializer


# Create your views here.

class LogoAIPView(ListAPIView):
    queryset = Logo.objects.all()
    serializer_class = LogoSerializer