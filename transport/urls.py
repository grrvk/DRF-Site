from django.urls import path
from . import views

urlpatterns = [
    path('', views.TransportListCreateView.as_view(), name='transport-list'),
    path('<int:pk>/update/', views.TransportUpdateApiView.as_view(), name='transport-edit'),
    path('<int:pk>/delete/', views.TransportDestroyApiView.as_view()),
    path('<int:pk>/', views.TransportDetailApiView.as_view(), name='transport-detail'),
]
