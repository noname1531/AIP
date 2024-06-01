from django.urls import path

from .views import *

urlpatterns = [
    path('', TaskAPIViwe.as_view(), name='task_aip'),
    path('create/', TaskAPICreate.as_view(), name='task_create_aip'),
    path('<int:pk>/', TaskAPIRetrieve.as_view(), name='task_retrieve_aip'),
    path('update/<int:pk>/', TaskAPIUpdate.as_view(), name='task-update_aip'),
    path('delete/<int:pk>/', TaskAPIDestroy.as_view(), name='task_delete_aip'),  
]