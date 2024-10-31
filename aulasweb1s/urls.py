
from django.urls import path
from . import views

urlpatterns = [
    path('', views.entry_list, name='entry_list'),
    path('<int:pk>/', views.entry_detail, name='entry_detail'),  
]
