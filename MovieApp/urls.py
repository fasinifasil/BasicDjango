
from django.urls import path

from MovieApp import views

urlpatterns = [
    path('',views.ListFunction,name='list'),
    path('edit',views.EditFunction,name='edit'),
    path('create',views.CreateFunction,name='create')
]