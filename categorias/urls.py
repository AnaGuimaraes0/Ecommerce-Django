from django.urls import path
from categorias import views

urlpatterns = [    
    path('', views.home, name='home'),    
]
