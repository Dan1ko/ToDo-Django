from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.login, name='login'),
    path('index', views.index, name='index'),
    # path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('add', views.addTodo, name='add'),
    path('complete/<todo_id>', views.completeTodo, name='complete'),
    path('deletecomplete', views.deleteCompleted, name='deletecomplete'),
    path('deleteall', views.deleteAll, name='deleteall'),
]