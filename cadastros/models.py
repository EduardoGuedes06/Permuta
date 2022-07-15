from tkinter import PROJECTING
from django.db import models
from django.contrib.auth.models import User


class Paciente(models.Model):
    cns = models.CharField(max_length=19, unique=True, verbose_name="Cartao Sus")
    nome = models.CharField(max_length=255, verbose_name="Nome")
    dataNascimento = models.DateField(verbose_name="Data de Nascimento")
    telefone = models.CharField(max_length=15)
    altura = models.CharField(max_length=4, verbose_name="Altura")
    peso = models.CharField(max_length=6, verbose_name="Peso")
    createdBy_user = models.ForeignKey(User, models.PROTECT, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.nome)


class UnidadeSolicitante(models.Model):
    cnes = models.CharField(max_length=7, verbose_name="Codigo do CNES")
    nome = models.CharField(max_length=50, verbose_name="Nome da Unidade")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.nome)


class UnidadeExecutante(models.Model):
    cnes = models.CharField(max_length=7, verbose_name="Codigo do CNES")
    nome = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.nome)


class Procedimento(models.Model):
    nome = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.nome)


class VagaOfertada(models.Model):
    tipo_choices = (
        ("EXAME", "EXAME"),
        ("CONSULTA", "CONSULTA")
    )

    tipo = models.CharField(max_length=10, choices=tipo_choices, blank=True, null=False, verbose_name="Tipo")
    paciente = models.ForeignKey(Paciente, on_delete=models.PROTECT, null=True, blank=True,
                                 verbose_name="Nome do Paciente")
    data_vagaOfertada = models.DateField(verbose_name="Data")
    hora_vagaOfertada = models.TimeField(verbose_name="Hora")
    procedimento = models.ForeignKey(Procedimento, on_delete=models.PROTECT, null=True, blank=True,
                                     verbose_name="Procedimento")
    unidadeExecutante = models.ForeignKey(UnidadeExecutante, on_delete=models.PROTECT, null=True, blank=True,
                                          verbose_name="Unidade Executante")
    unidadeSolicitante = models.OneToOneField(UnidadeSolicitante, on_delete=models.PROTECT, null=True, blank=True)
    motivo = models.CharField(max_length=100)
    solicitacao = models.CharField(max_length=12, verbose_name="Código da Solicitação")
    status = models.BooleanField(default=False, null=True, blank=True, editable=False)
    createdBy_user = models.ForeignKey(User, models.PROTECT, default=1, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = "Vagas Ofertadas"

    def __str__(self):
        return "{} | Paciente: {}".format(self.procedimento.nome, self.paciente.nome)


class Permuta(models.Model):
    nomePacienteAgendado = models.ForeignKey(Paciente, on_delete=models.PROTECT, null=True, blank=True, unique=False,
                                             related_name="nomePacienteAgendado", verbose_name="Paciente Para Agendar")
    nomePacienteOfertado = models.ForeignKey(Paciente, on_delete=models.PROTECT, null=True, blank=True, unique=False,
                                             related_name="nomePacienteOfertado")
    data_vagaOfertada = models.DateTimeField(verbose_name="Data")
    hora_vagaOfertada = models.TimeField(verbose_name="Hora")
    procedimento = models.ForeignKey(Procedimento, on_delete=models.PROTECT, verbose_name="Procedimento")
    unidadeExecutante = models.ForeignKey(UnidadeExecutante, on_delete=models.PROTECT,
                                          verbose_name="Unidade Executante")
    motivo = models.CharField(max_length=255, null=True, blank=True)
    createdBy_user = models.ForeignKey(User, models.PROTECT, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return "{}".format(self.nomePacienteAgendado.nome)

class UserUnidade(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT, unique=False, verbose_name="Usuários")
    unidadeSolicitante = models.ForeignKey(UnidadeSolicitante, on_delete=models.PROTECT, verbose_name="Local de Trabalho", unique=False)

    def __str__(self):
        return "{}".format(self.user.first_name)

class Log(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    target_id = models.PositiveBigIntegerField()
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
