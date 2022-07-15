from django.urls import path
from .views import PaginaInicial, SobreView


urlpatterns = [
    #path('endereço/', MinhaView.as_view(), name = 'nome-da-url'),   
    #path('',IndexView.as_view(), name = 'index'), 
     path('',PaginaInicial.as_view(),name = 'index'), 
     path('sobre/',SobreView.as_view(), name ='sobre')
]     