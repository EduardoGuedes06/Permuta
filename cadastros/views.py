from audioop import reverse
from typing import Container
from wsgiref.simple_server import server_version
from django.http import JsonResponse, HttpRequest
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from django.db import transaction
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


from .models import Paciente, UnidadeSolicitante, UnidadeExecutante, Procedimento,VagaOfertada, Permuta

from django.urls import reverse_lazy

from .forms import PermutarForm
from braces.views import GroupRequiredMixin

#Create your views here

################## Create ################
class PacienteCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('userLogin')
    group_required = [u"administrator", u"callcenter"]
    model = Paciente
    fields = ['cns', 'nome', 'dataNascimento', 'telefone','altura', 'peso']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-paciente')

class UnidadeSolicitanteCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('userLogin')
    group_required = [u"administrator", u"callcenter"]
    model = UnidadeSolicitante
    fields =['cnes','nome']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-unidsol')

class UnidadeExecutanteCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('userLogin')
    group_required = [u"administrator", u"callcenter"]
    model = UnidadeExecutante
    fields =['cnes','nome']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-unidexec')

class ProcedimentoCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('userLogin')
    group_required = [u"administrator", u"callcenter"]
    model = Procedimento
    fields = ['nome']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-procedimento')

class VagaOfertadaCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('userLogin')    
    group_required = [u"administrator", u"callcenter", u"administrativo"]
    model = VagaOfertada
    fields =['paciente','data_vagaOfertada','hora_vagaOfertada','tipo','procedimento', 'unidadeExecutante','solicitacao', 'motivo']
    template_name ='cadastros/CadVagOf.html'
    success_url = reverse_lazy('listar-vagaofertada')

    def form_valid(self, form):
        form.instance.createdBy_user = self.request.user
        url = super().form_valid(form)
        return url


class PermutaCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('userLogin')
    group_required = [u"administrator", u"callcenter"]
    model = Permuta
    fields = ["nomePacienteAgendado","nomePacienteOfertado","data_vagaOfertada","hora_vagaOfertada","procedimento","unidadeExecutante","motivo"]
    template_name = "cadastros/CadVagOf.html"
    success_url = reverse_lazy('listar-permuta')


################## UpDate ################
class PacienteUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('userLogin')
    group_required = [u"administrator", u"callcenter"]
    model = Paciente
    fields = ['cns','nome','dataNascimento','telefone','altura','peso']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-paciente')


class UnidadeSolicitanteUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('userLogin')
    group_required = [u"administrator", u"callcenter"]
    model = UnidadeSolicitante
    fields =['cnes','nome']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-unidsol')


class UnidadeExecutanteUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('userLogin')
    group_required = [u"administrator", u"callcenter"]
    model = UnidadeExecutante
    fields =['cnes','nome']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-unidexec')


class ProcedimentoUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('userLogin')
    group_required = [u"administrator", u"callcenter"]
    model = Procedimento
    fields = ['nome']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-procedimento')


class VagaOfertadaUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('userLogin')
    group_required = [u"administrator", u"callcenter", u"administrativo"]
    model = VagaOfertada
    fields =['paciente','data_vagaOfertada','hora_vagaOfertada','tipo','procedimento', 'unidadeExecutante','solicitacao', 'motivo']
    template_name ='cadastros/CadVagOf.html'
    success_url = reverse_lazy('listar-vagaofertada')

    def form_valid(self, form):
        form.instance.createdBy_user = self.request.user
        url = super().form_valid(form)
        return url

class PermutaUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('userLogin')
    group_required = [u"administrator", u"callcenter"]

    def get(self, request, *args, **kwargs):        
        form = PermutarForm()
        vagaOfertada = get_object_or_404(VagaOfertada, pk = kwargs['id'])
        pacientes = Paciente.objects.all()
        return render(request, 'cadastros/showPermuta.html', { 'vagaOfertada': vagaOfertada, "pacientes": pacientes, "form": form })


################## Delete ################
class PacienteDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('userLogin')
    group_required = [u"administrator", u"callcenter"]
    model = Paciente
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-paciente')


class UnidadeSolicitanteDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('userLogin')
    group_required = [u"administrator", u"callcenter"]
    model = UnidadeSolicitante
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-unidsol')


class UnidadeExecutanteDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('userLogin')
    group_required = [u"administrator", u"callcenter"]
    model = UnidadeExecutante
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-unidexec')


class ProcedimentoDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('userLogin')
    group_required = [u"administrator", u"callcenter"]
    model = Procedimento
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-procedimento')


class VagaOfertadaDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('userLogin')
    group_required = [u"administrator", u"callcenter", u"administrativo"]
    model = VagaOfertada
    template_name ='cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-vagaofertada')


################## List ################
class PacienteList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    # paginate_by = 10
    login_url = reverse_lazy('userLogin')
    group_required = [u"administrator", u"callcenter"]
    model = Paciente
    template_name = 'cadastros/listas/paciente.html'
    success_url = reverse_lazy('listar-paciente')


class UnidadeSolicitanteList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    # paginate_by = 10
    login_url = reverse_lazy('userLogin')
    group_required = [u"administrator", u"callcenter"]
    model = UnidadeSolicitante
    template_name = 'cadastros/listas/unidsol.html'


class UnidadeExecutanteList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    # paginate_by = 10
    login_url = reverse_lazy('userLogin')    
    group_required = [u"administrator", u"callcenter"]
    model = UnidadeExecutante
    template_name = 'cadastros/listas/unidexec.html'
    success_url = reverse_lazy('index')


class ProcedimentoList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    # paginate_by = 10
    login_url = reverse_lazy('userLogin')
    group_required = [u"administrator", u"callcenter"]
    model = Procedimento
    template_name = 'cadastros/listas/procedimento.html'
    success_url = reverse_lazy('index')


class VagaOfertadaList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    # paginate_by = 10
    login_url = reverse_lazy('userLogin')
    group_required = [u"administrator", u"callcenter", u"administrativo"]
    model = VagaOfertada
    template_name ='cadastros/listas/ListVagOf.html'
    success_url = reverse_lazy('index')
    


class PermutaList(GroupRequiredMixin,LoginRequiredMixin, ListView):    
    login_url = reverse_lazy('userLogin')    
    group_required = [u"administrator", u"callcenter"]
    # model = Permuta    
    # template_name ='cadastros/listas/listarPermutas.html'
    # success_url = reverse_lazy('listar_permutas', {"vagas": vagas})
    def get(self, request):
        vagas = VagaOfertada.objects.all()        
        return render(request, 'cadastros/listas/listarPermutas.html', { 'vagas': vagas })     


# @login_required(login_url='userLogin')
# def permutaList(request):
#     vagas = VagaOfertada.objects.all()
#     return render(request, 'cadastros/listas/listarPermutas.html', { 'vagas': vagas })

@login_required(login_url='userLogin')
def showPermuta(request, id):
    form = PermutarForm()
    vagaOfertada = get_object_or_404(VagaOfertada, pk = id)
    pacientes = Paciente.objects.all()
    return render(request, 'cadastros/showPermuta.html', { 'vagaOfertada': vagaOfertada, "pacientes": pacientes, "form": form })


@transaction.atomic
def permutaStore(request: HttpRequest):
    with transaction.atomic():
        if request.method == 'POST':
            vaga = VagaOfertada.objects.get(pk = request.POST.get('vaga'))        
            Permuta.objects.create(
                data_vagaOfertada = request.POST.get('data_vagaOfertada'),
                hora_vagaOfertada = request.POST.get('hora_vagaOfertada'),
                procedimento = Procedimento.objects.get(id = request.POST.get('procedimento')),
                # data_inclusao = request.POST.get('data_inclusao'),
                unidadeExecutante = UnidadeExecutante.objects.get(id = request.POST.get('unidadeExecutante')),
                motivo = request.POST.get('motivo'),
                nomePacienteAgendado_id = request.POST.get('nomePacienteAgendado'),
                nomePacienteOfertado_id = request.POST.get('nomePacienteOfertado')
            )
            
            vaga.status = True
            vaga.save()
            vagaStatus = vagaDestroy(request, vaga)

            message = "Permuta efetuada!"        
            return redirect('listar_permutas')
    return redirect('index')           


@transaction.atomic
def vagaDestroy(request, vaga):    
    with transaction.atomic():
        if request.method == 'POST':
            vaga.delete()
            return True
        return False