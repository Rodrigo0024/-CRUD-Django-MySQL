from django.contrib import admin
from django.urls import path
from tarefas import views

from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.listar_tarefas, name='listar_tarefas'),
    path('nova/', views.criar_tarefa, name='criar_tarefa'),
    path('deletar/<int:id>/', views.deletar_tarefa, name='deletar_tarefa'),
    
    # Autenticação
    path('cadastro/', views.cadastrar, name='cadastrar'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('editar/<int:id>/', views.editar_tarefa, name='editar_tarefa'),
    path('deletar/<int:id>/', views.deletar_tarefa, name='deletar_tarefa'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)