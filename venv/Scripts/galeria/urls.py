from django.urls import path
from Scripts.galeria.views import index , imagem


urlpatterns = [
path('',index),
path('imagem/', imagem , name= 'imagem'),
]