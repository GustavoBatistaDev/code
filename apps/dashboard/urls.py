from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.lista_avaliacoes, name='dashboard'),
    path('avaliacao/', views.cadastro_avaliacao, name='avaliacao'),
    path('editar_avaliacao/<int:id>', views.editar_avaliacao, name='editar_avaliacao'),
    path('deletar_avaliacao/<int:id>', views.deletar_avaliacao, name='deletar_avaliacao'),
    path('form_avaliacao/', views.form_avaliacao, name='form_avaliacao'),
    path('crise/', views.crise, name='crise'),
    path('contato/', views.contato, name='contato'),
    path('ajuda/', views.ajuda, name='ajuda'),
]
