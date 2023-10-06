from django.urls import path
from app2 import views

urlpatterns = [
    path('view2/', views.view2, name='view2'),
]