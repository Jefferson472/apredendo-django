from django.shortcuts import render
from passagens.forms import PassagemForm


def index(request):
    form = PassagemForm()
    contexto = {'form': form}
    return render(request, 'index.html', contexto)


def minha_consulta(request):
    if request.method == 'POST':
        form = PassagemForm(request.POST)
        if form.is_valid():
            contexto = {'form': form}
            return render(request, 'minha_consulta.html', contexto)
        else:
            contexto = {'form': form}
            return render(request, 'index.html', contexto)
