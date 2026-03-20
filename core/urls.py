from django.contrib import admin
from django.urls import path
from tarefas import views

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.listar_tarefas, name='listar_tarefas'),
    path('nova/', views.criar_tarefa, name='criar_tarefa'),
    path('deletar/<int:id>/', views.deletar_tarefa, name='deletar_tarefa'),
    
    # Autenticação
    path('cadastro/', views.cadastrar, name='cadastrar'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]