from django.urls import path
from . import views

app_name = 'dashboard'


urlpatterns = [
    path('', views.index, name="index"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('avaliacao/', views.cadastro_avaliacao, name='avaliacao')
]
