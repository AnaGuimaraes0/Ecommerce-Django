from django.urls import path
from . import views



urlpatterns = [
    path('admin/', views.home_produtos, name='home_produtos'),
    path('entrar/', views.login_cliente, name='login_cliente'),
    # path('sair/', views.login_cliente, name='login_cliente'),

]