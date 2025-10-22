from django.shortcuts import render, redirect, get_object_or_404
from main.models import Quarto, Reserva
# Create your views here.
def index(request):
    return render(request, 'main/index.html')


def agendamento(request):
    return render(request, 'main/agendamento.html')

# def checar_quarto(request, id_quarto):
#     quarto = get_object_or_404(Quarto, id=id_quarto)
#     reservas = Reserva.objects.filter(quarto=quarto)
#     if quarto.capacidade <= len(reservas):
#         return redirect('index')
#     context = {'quarto': quarto, 'reservas': len(reservas), 'capacidade': quarto.capacidade}
#     return render(request, 'main/teste.html', context)
def quartos_disponiveis(request):
    quartos = Quarto.objects.all()
    l = []
    for i in quartos:
        reservas = Reserva.objects.filter(quarto=i)
        if i.capacidade > len(reservas):
            l.append(i)
    context = {'quartos': l}
    return render(request, 'main/disponiveis.html', context)
def detalhes(request, id_quarto):
    quarto = get_object_or_404(Quarto, id=id_quarto)
    context = {'quarto': quarto}
    return render(request, 'main/detalhes.html', context)

def reservar(request, id_quarto):
    quarto = get_object_or_404(Quarto, id=id_quarto)
    reservas = Reserva.objects.filter(quarto=quarto)
    if quarto.capacidade <= len(reservas):
        mensagem = "Quarto cheio"
        return redirect('index')
    else: 
        if request.method == 'POST':
            nome_hospede = request.POST.get('nome')
            telefone = request.POST.get('telefone')
            data_entrada = request.POST.get('data_entrada')
            data_saida = request.POST.get('data_saida')
            reserva = Reserva(quarto=quarto, nome_hospede=nome_hospede, telefone=telefone, data_entrada=data_entrada, data_saida=data_saida)
            reserva.save()
            return redirect('disponivel')
    context = {'quarto': quarto}
    return render(request, 'main/reservas.html', context)