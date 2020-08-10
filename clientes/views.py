from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator

from .models import Cliente
from aluguels.models import Aluguel
from .forms import ClienteForm


@login_required
def index(request):
    clientes_list = Cliente.objects.all()
    paginator = Paginator(clientes_list, 5)
    page = request.GET.get('page')
    clientes = paginator.get_page(page)
    return render(request, 'clientes/index.html', {'clientes': clientes})


@login_required
def detalhe(request, id):
    cliente = get_object_or_404(Cliente, pk=id)
    aluguels = Aluguel.objects.filter(cliente=id)
    return render(request, 'clientes/detalhe.html', {'cliente': cliente, 'aluguels': aluguels})


@login_required
def adicionar(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente adicionado com sucesso!')
            return redirect('/cliente')
        else:
            messages.warning(request, 'Ocorreu um erro! Tente novamente!')
            return render(request, 'clientes/adicionar.html', {'form': form})
    else:
        form = ClienteForm()
        return render(request, 'clientes/adicionar.html', {'form': form})


@login_required
def editar(request, id):
    cliente = get_object_or_404(Cliente, pk=id)
    form = ClienteForm(instance=cliente)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente atualizado com sucesso!')
            return redirect('/cliente')
        else:
            messages.warning(request, 'Ocorreu um erro! Tente novamente!')
            return render(request, 'clientes/editar.html', {'form': form, 'cliente': cliente})
    else:
        return render(request, 'clientes/editar.html', {'form': form, 'cliente': cliente})


@login_required
def deletar(request, id):
    cliente = get_object_or_404(Cliente, pk=id)
    cliente.delete()
    messages.success(request, 'Cliente deletado com sucesso!')
    return redirect('/cliente')
