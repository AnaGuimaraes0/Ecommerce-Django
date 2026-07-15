from django.urls import path
from clientes import views

urlpatterns = [    
    path('', views.clientes_view, name='clientes'),    
]