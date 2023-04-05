from django.urls import path
from . import views

app_name = 'menu'

urlpatterns = [
    path('', views.index),
    path('<item_id>/', views.detail_page, name='detail'),
]