from django.urls import path
from . import views

app_name = 'order'

urlpatterns = [
    path('', views.OrderListView.as_view(), name='list'),
    path('create/', views.OrderCreateView.as_view(), name='create'),
    path('<int:pk>/delete/', views.OrderDeleteView.as_view(), name='delete'),
]
