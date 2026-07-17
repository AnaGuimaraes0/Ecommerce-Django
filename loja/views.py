from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required, permission_required
from .form import FormularioLoginCliente

def login_cliente(request):
    if request.user.is_authenticated:
        return redirect('home_produtos')
    
    if request.method == 'POST':
        form = FormularioLoginCliente(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            usuario = authenticate(username=username, password=password)

            if usuario is not None:
                login(request, usuario)

                redirect_to = request.GET.get('next', 'home_produtos')
                return redirect(redirect_to)
    else:
        form = FormularioLoginCliente()
    
    return render(request, 'loja/login.html', {'form': form})

def logout_cliente(request):
    logout(request)
    return redirect('home_produtos')


def home_produtos(request):
    return render(request, 'loja/home.html')

@login_required(login_url='login_cliente')
@permission_required('loja.view_relatorio_vendas', login_url='acesso_negado', raise_exception=False)
def painel_financeiro(request):
    return render(request, 'loja/painel_financeiro.html')

def acesso_negado(request):
    return render(request, 'loja/acesso-negado.html')