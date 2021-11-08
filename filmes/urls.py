from django.urls import path
from . import views

urlpatterns = [
    path('minhalista/<int:filme_id>/', views.api_filme),
    # path('', views.api_filme)
]