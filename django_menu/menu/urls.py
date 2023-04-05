from django.urls import path
from . import views

app_name = 'menu'

urlpatterns = [
    path('', views.index),
    path('<int:item_id>/', views.detail_page, name='detail'),
]
