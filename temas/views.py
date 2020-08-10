from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator

from .models import Tema
from items.models import Item
from .forms import TemaForm


def welcome(request):
    return render(request, 'welcome.html')


@login_required
def index(request):
    temas_list = Tema.objects.all()
    paginator = Paginator(temas_list, 5)
    page = request.GET.get('page')
    temas = paginator.get_page(page)
    return render(request, 'temas/index.html', {'temas': temas})


@login_required
def detalhe(request, id):
    tema = get_object_or_404(Tema, pk=id)
    items = Item.objects.filter(tema=id)
    return render(request, 'temas/detalhe.html', {'tema': tema, 'items': items})


@login_required
def adicionar(request):
    if request.method == 'POST':
        form = TemaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tema adicionado com sucesso!')
            return redirect('/tema')
        else:
            messages.warning(request, 'Ocorreu um erro! Tente novamente!')
            return render(request, 'temas/adicionar.html', {'form': form})
    else:
        form = TemaForm()
        return render(request, 'temas/adicionar.html', {'form': form})


@login_required
def editar(request, id):
    tema = get_object_or_404(Tema, pk=id)
    form = TemaForm(instance=tema)
    if request.method == 'POST':
        form = TemaForm(request.POST, instance=tema)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tema atualizado com sucesso!')
            return redirect('/tema')
        else:
            messages.warning(request, 'Ocorreu um erro! Tente novamente!')
            return render(request, 'temas/editar.html', {'form': form, 'tema': tema})
    else:
        return render(request, 'temas/editar.html', {'form': form, 'tema': tema})


@login_required
def deletar(request, id):
    tema = get_object_or_404(Tema, pk=id)
    tema.delete()
    messages.success(request, 'Tema deletado com sucesso!')
    return redirect('/tema')
