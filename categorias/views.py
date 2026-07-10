from django.shortcuts import render
from .models import Categoria

def home(request):
    categorias = Categoria.object.all()
    return render('categoria/index.html', {'categorias': categorias})