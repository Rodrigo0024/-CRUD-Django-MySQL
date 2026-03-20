from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Tarefa

@login_required
def listar_tarefas(request):
    tarefas = Tarefa.objects.filter(usuario=request.user)
    return render(request, 'tarefas/lista.html', {'tarefas': tarefas})

@login_required
def criar_tarefa(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        Tarefa.objects.create(usuario=request.user, titulo=titulo, descricao=descricao)
        return redirect('listar_tarefas')
    return render(request, 'tarefas/form.html')

@login_required
def deletar_tarefa(request, id):
    tarefa = get_object_or_404(Tarefa, id=id, usuario=request.user)
    tarefa.delete()
    return redirect('listar_tarefas')


from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def cadastrar(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) # Loga automaticamente após cadastrar
            return redirect('listar_tarefas')
    else:
        form = UserCreationForm()
    return render(request, 'registration/cadastro.html', {'form': form})