from django.urls import path

from .views import *

urlpatterns = [
    path('', NewsAPIViwe.as_view(), name='news_aip'),
    path('create/', NewsAPICreate.as_view(), name='news_create_aip'),
    path('<int:pk>/', NewsAPIRetrieve.as_view(), name='news_retrieve_aip'),
    path('update/<int:pk>/', NewsAPIUpdate.as_view(), name='news_update_aip'),
    path('delete/<int:pk>/', NewsAPIDestroy.as_view(), name='news_delete_aip'),  
]