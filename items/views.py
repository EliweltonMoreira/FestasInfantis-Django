from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Item
from temas.models import Tema
from .forms import ItemForm


@login_required
def adicionar(request, id):
    tema = get_object_or_404(Tema, pk=id)
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.tema = tema
            item.save()
            messages.success(request, 'Item adicionado com sucesso!')
            return redirect('tema.detalhe', id=id)
        else:
            messages.warning(request, 'Ocorreu um erro! Tente novamente!')
            return render(request, 'items/adicionar.html', {'form': form, 'tema': tema})
    else:
        form = ItemForm()
        return render(request, 'items/adicionar.html', {'form': form, 'tema': tema})


@login_required
def editar(request, id):
    item = get_object_or_404(Item, pk=id)
    form = ItemForm(instance=item)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, 'Item atualizado com sucesso!')
            return redirect('tema.detalhe', id=item.tema.id)
        else:
            messages.warning(request, 'Ocorreu um erro! Tente novamente!')
            return render(request, 'items/editar.html', {'form': form, 'item': item})
    else:
        return render(request, 'items/editar.html', {'form': form, 'item': item})


@login_required
def deletar(request, id):
    item = get_object_or_404(Item, pk=id)
    item.delete()
    messages.success(request, 'Item deletado com sucesso!')
    return redirect('tema.detalhe', id=item.tema.id)
