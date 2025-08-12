from django.shortcuts import render, get_object_or_404, redirect
import datetime
from .models import DatasEventos
from .forms import Minha_Forms
# Create your views here.
def datahj():
    data_hoje = datetime.date.today()
    data_hoje = data_hoje.strftime("%d/%m/%Y")
    data_hoje = str(data_hoje)
    return data_hoje

def tarefaspendentes():
    eventos = DatasEventos.objects.all()
    cont = 0
    for i in eventos:
        if i.status == False:
            cont += 1
    return cont

def index(request):
    eventos = DatasEventos.objects.all().order_by("prioridade")
    context = {'data_hoje': datahj(), 'eventos': eventos, 'tarefaspendentes': tarefaspendentes()}
    return render(request, 'index.html', context=context)

def detalhes(request, id):
    evento = get_object_or_404(DatasEventos,id=id)
    contexto = {'evento': evento, 'data_hoje': datahj(), 'tarefaspendentes': tarefaspendentes()}
    if request.method == "POST":
        print(request.POST)
        if 'status' in request.POST:
            evento.status = True
            
        else:
            evento.status = False
        evento.save()

        return redirect('detalhes_evento', id = evento.id)
    return render(request, 'detalhes.html', contexto)
def excluir(request, id):
    evento = get_object_or_404(DatasEventos,id=id)
    evento.delete()
    return redirect("index")
def criar_eventos(request):
    if request.method == "POST":
        form = Minha_Forms(request.POST)
        if form.is_valid():
            form.save()
            form = Minha_Forms()
            context = {'form': form}
            return render(request, "criar.html", context)
        else:
            context = {'form': form}

            return render(request, "criar.html", context)
            
    else:
        form = Minha_Forms()
        context = {'form': form}
        return render(request, "criar.html", context)
    