from django.urls import path

from .views import LogoAIPView

urlpatterns = [
    path('', LogoAIPView.as_view(), name='logo_aip'),
]