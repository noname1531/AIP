from django.urls import path

from .views import *

urlpatterns = [
    path('', TeamAPIViwe.as_view(), name='team_aip'),
    path('team/', TeamAPICreate.as_view(), name='team_create_aip'),
    path('<int:pk>/', TeamAPIRetrieve.as_view(), name='team_retrieve_aip'),
    path('update/<int:pk>/', TeamAPIUpdate.as_view(), name='team_update_aip'),
    path('delete/<int:pk>/', TeamAPIDestroy.as_view(), name='team_delete_aip'),  
]