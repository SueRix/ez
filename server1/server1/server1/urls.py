from django.urls import path
from app1 import views

urlpatterns = [
    path('', views.view1, name='view1'),
    path('view1/', views.view1, name='view1'),
]