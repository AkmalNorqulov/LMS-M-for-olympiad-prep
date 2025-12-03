from django.urls import path
from . import views

app_name = 'schedule'

urlpatterns = [
    path('', views.index, name='index'),
    path('day/<int:day>/', views.day_detail, name='day'),
]
