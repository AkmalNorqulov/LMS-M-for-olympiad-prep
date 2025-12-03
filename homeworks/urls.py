from django.urls import path
from .views import homeworks, add_homework, delete_homework

app_name = 'homeworks'

urlpatterns = [
    path('', homeworks, name='homeworks'),
    path('add/', add_homework, name='add_homework'),
    path('<int:pk>/delete/', delete_homework, name='delete_homework'),
]