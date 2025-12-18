from django.shortcuts import render, redirect, get_object_or_404
from .models import Movel

def index(request):
    return render(request, 'index.html')

def listar(request):
    moveis = Movel.objects.order_by('comodo', 'nome')
    return render(request, 'listar.html', {'moveis': moveis})

def novo(request):
    if request.method == 'POST':
        Movel.objects.create(
            nome=request.POST['nome'],
            comodo=request.POST['comodo'],
            preco=request.POST['preco'],
            data_compra=request.POST.get('data_compra')
        )
        return redirect('listar')

    return render(request, 'novo.html')

def editar(request, id):
    movel = get_object_or_404(Movel, id=id)

    if request.method == 'POST':
        movel.nome = request.POST['nome']
        movel.comodo = request.POST['comodo']
        movel.preco = request.POST['preco']
        movel.data_compra = request.POST.get('data_compra')
        movel.save()
        return redirect('listar')

    return render(request, 'editar.html', {'movel': movel})

def excluir(request, id):
    movel = get_object_or_404(Movel, id=id)
    movel.delete()
    return redirect('listar')

def relatorios(request):
    moveis = Movel.objects.all()

    total_geral = sum(m.preco for m in moveis)

    total_por_comodo = {}
    for m in moveis:
        total_por_comodo[m.comodo] = total_por_comodo.get(m.comodo, 0) + m.preco

    return render(request, 'relatorios.html', {
        'total_geral': total_geral,
        'total_por_comodo': total_por_comodo
    })