import django
from django.views.generic import TemplateView

#Create your views here
#class IndexView(TemplateView):
# template_name = 'modelo.html'

#class PaginaInicial(TemplateView):
#     template_name = "modelo.html"


# A classe PaginaInicial "extends" TemplateView
class PaginaInicial(TemplateView):
    # Toda classe filha do TemplateView precisa do
    # atributo abaixo para definir um template a ser renderizado
    template_name = 'paginas/index2.html'
 

class SobreView(TemplateView):
   template_name = 'paginas/sobre.html'