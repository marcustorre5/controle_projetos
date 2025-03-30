# projetos/views.py
from django.shortcuts import render, redirect
from .forms import ProjetoForm
from .models import Projeto  # Adicione essa importação para acessar os projetos
from django.shortcuts import render, get_object_or_404
from .models import Projeto
from django.shortcuts import redirect
from django.shortcuts import render, redirect
from .forms import ProjetoForm
from django.shortcuts import render
from .models import Projeto


# Função para exibir os detalhes de um projeto
def detalhes_projeto(request, pk):
    projeto = get_object_or_404(Projeto, pk=pk)  # Obtém o projeto pelo ID (pk)
    return render(request, 'projetos/detalhes_projeto.html', {'projeto': projeto})

# Função para adicionar um novo projeto
def adicionar_projeto(request):
    if request.method == 'POST':
        form = ProjetoForm(request.POST)
        if form.is_valid():
            form.save()  # Salva o projeto no banco de dados
            return redirect('projetos:lista_projetos')  # Redireciona para a lista de projetos
    else:
        form = ProjetoForm()
    return render(request, 'projetos/adicionar_projeto.html', {'form': form})

# Função para listar os projetos
def lista_projetos(request):
    projetos = Projeto.objects.all()  # Obtém todos os projetos do banco de dados
    return render(request, 'projetos/lista.html', {'projetos': projetos})

def home(request):
    return redirect('projetos:lista_projetos')  # Redireciona para a lista de projetos

def adicionar_projeto(request):
    if request.method == 'POST':
        form = ProjetoForm(request.POST)
        if form.is_valid():
            form.save()  # Salva o projeto no banco de dados
            return redirect('projetos:lista_projetos')  # Redireciona para a lista de projetos
    else:
        form = ProjetoForm()
    return render(request, 'projetos/adicionar_projeto.html', {'form': form})

def index(request):
    return render(request, 'projetos/index.html')

def lista_projetos(request):
    projetos = Projeto.objects.all()  # Obtém todos os projetos
    return render(request, 'projetos/lista_projetos.html', {'projetos': projetos})
