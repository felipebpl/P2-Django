from django.urls import path
from . import views

urlpatterns = [
    path('<int:filme_id>/', views.api_filme),
    # path('', views.api_filme)
]