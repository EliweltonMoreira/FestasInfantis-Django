from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Aluguel
from clientes.models import Cliente
from .forms import AluguelForm


@login_required
def adicionar(request, id):
    cliente = get_object_or_404(Cliente, pk=id)
    if request.method == 'POST':
        form = AluguelForm(request.POST)
        if form.is_valid():
            aluguel = form.save(commit=False)
            aluguel.cliente = cliente
            aluguel.save()
            messages.success(request, 'Aluguel adicionado com sucesso!')
            return redirect('cliente.detalhe', id=id)
        else:
            messages.warning(request, 'Ocorreu um erro! Tente novamente!')
            return render(request, 'aluguels/adicionar.html', {'form': form, 'cliente': cliente})
    else:
        form = AluguelForm()
        return render(request, 'aluguels/adicionar.html', {'form': form, 'cliente': cliente})


@login_required
def editar(request, id):
    aluguel = get_object_or_404(Aluguel, pk=id)
    form = AluguelForm(instance=aluguel)
    if request.method == 'POST':
        form = AluguelForm(request.POST, instance=aluguel)
        if form.is_valid():
            form.save()
            messages.success(request, 'Aluguel atualizado com sucesso!')
            return redirect('cliente.detalhe', id=aluguel.cliente.id)
        else:
            messages.warning(request, 'Ocorreu um erro! Tente novamente!')
            return render(request, 'aluguels/editar.html', {'form': form, 'aluguel': aluguel})
    else:
        return render(request, 'aluguels/editar.html', {'form': form, 'aluguel': aluguel})


@login_required
def deletar(request, id):
    aluguel = get_object_or_404(Aluguel, pk=id)
    aluguel.delete()
    messages.success(request, 'Aluguel deletado com sucesso!')
    return redirect('cliente.detalhe', id=aluguel.cliente.id)
