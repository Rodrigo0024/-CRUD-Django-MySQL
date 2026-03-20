from django.db import models
from django.contrib.auth.models import User

class Tarefa(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    descricao = models.TextField(blank=True, null=True)
    concluida = models.BooleanField(default=False)
    criado_em = models.DateTimeField(auto_now_add=True)
    arquivo_pdf = models.FileField(upload_to='pdfs/', null=True, blank=True)
    resumo = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.titulo

