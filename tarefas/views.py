from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Tarefa

@login_required
def listar_tarefas(request):
    tarefas = Tarefa.objects.filter(usuario=request.user)
    return render(request, 'tarefas/lista.html', {'tarefas': tarefas})

import PyPDF2
from django.shortcuts import render, redirect

def extrair_resumo_pdf(arquivo):
    leitor = PyPDF2.PdfReader(arquivo)
    texto_completo = ""
    # Lê as primeiras 3 páginas para não sobrecarregar
    for pagina in leitor.pages[:3]:
        texto_completo += pagina.extract_text()
    
    # Aqui você poderia integrar com uma API de IA. 
    # Por enquanto, faremos um resumo básico das primeiras linhas:
    resumo_gerado = texto_completo[:500] + "..." 
    return resumo_gerado

@login_required
def criar_tarefa(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        pdf = request.FILES.get('arquivo_pdf') # Pega o arquivo
        
        resumo = ""
        if pdf:
            resumo = extrair_resumo_pdf(pdf)

        Tarefa.objects.create(
            usuario=request.user, 
            titulo=titulo, 
            descricao=descricao,
            arquivo_pdf=pdf,
            resumo=resumo
        )
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


@login_required
def editar_tarefa(request, id):

    tarefa = get_object_or_404(Tarefa, id=id, usuario=request.user)

    if request.method == 'POST':
        tarefa.titulo = request.POST.get('titulo')
        tarefa.descricao = request.POST.get('descricao')
        
        novo_pdf = request.FILES.get('arquivo_pdf')
        if novo_pdf:
            tarefa.arquivo_pdf = novo_pdf
            tarefa.resumo = extrair_resumo_pdf(novo_pdf) 

        tarefa.save()
        return redirect('listar_tarefas')

    return render(request, 'tarefas/form.html', {'tarefa': tarefa})


@login_required
def deletar_tarefa(request, id):
    tarefa = get_object_or_404(Tarefa, id=id, usuario=request.user)
    tarefa.delete()
    return redirect('listar_tarefas')