from django.urls import path
from . import views

urlpatterns = [
    path('', views.gotominhalista),
    path('minha-lista/', views.api_minhalista),
    path('minha-lista/<int:filme_id>/', views.api_filme),
]