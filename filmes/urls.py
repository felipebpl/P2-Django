from django.urls import path
from . import views

urlpatterns = [
    path('minhalista/', views.api_filme),
    path('minhalista/<int:filme_id>/', views.api_filme),
]