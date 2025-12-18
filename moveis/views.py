from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Movel
from .forms import MovelForm

def index(request):
    return render(request, 'index.html')

def listar(request):
    moveis = Movel.objects.order_by('comodo', 'nome')
    
    # Busca simples
    search = request.GET.get('search')
    if search:
        moveis = moveis.filter(
            nome__icontains=search
        ) | moveis.filter(
            comodo__icontains=search
        )
    
    return render(request, 'move_list.html', {'moveis': moveis})

def novo(request):
    if request.method == 'POST':
        form = MovelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Móvel cadastrado com sucesso!')
            return redirect('listar')
        else:
            messages.error(request, 'Erro ao cadastrar móvel. Verifique os dados.')
    else:
        form = MovelForm()
    
    return render(request, 'move_form.html', {'form': form, 'title': 'Adicionar Móvel'})

def editar(request, id):
    movel = get_object_or_404(Movel, id=id)
    
    if request.method == 'POST':
        form = MovelForm(request.POST, instance=movel)
        if form.is_valid():
            form.save()
            messages.success(request, 'Móvel atualizado com sucesso!')
            return redirect('listar')
        else:
            messages.error(request, 'Erro ao atualizar móvel. Verifique os dados.')
    else:
        form = MovelForm(instance=movel)
    
    return render(request, 'move_form.html', {'form': form, 'title': 'Editar Móvel', 'movel': movel})

def excluir(request, id):
    movel = get_object_or_404(Movel, id=id)
    nome_movel = movel.nome
    movel.delete()
    messages.success(request, f'Móvel "{nome_movel}" excluído com sucesso!')
    return redirect('listar')

def relatorios(request):
    moveis = Movel.objects.all()

    total_geral = sum(m.preco for m in moveis)

    total_por_comodo = {}
    for m in moveis:
        total_por_comodo[m.comodo] = total_por_comodo.get(m.comodo, 0) + m.preco

    return render(request, 'relatorios.html', {
        'moveis': moveis,
        'total_geral': total_geral,
        'total_por_comodo': total_por_comodo
    })