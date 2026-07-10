from django.shortcuts import render
from .models import Categoria

def home(request):
    categorias = Categoria.object.all()
    return render(request,'categoria/index.html', {'categorias': categorias})