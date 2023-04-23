from django.urls import path
from Scripts.galeria.views import index


urlpatterns = [
path('',index),
]