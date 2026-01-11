from django.shortcuts import render,redirect
from django.core.paginator import Paginator
import random
from .models import Numbers
from .forms import NumbersForm
# Create your views here.
def index(request):
    form = NumbersForm()
    if request.method == "POST":
        form = NumbersForm(request.POST)
        if form.is_valid():
            Numbers.objects.all().delete()
            form.save()
            if request.session.get('numeros'):
                del request.session['numeros']

            return redirect('sorteados')
    return render(request, "sortearprinci/index.html", {'form': form})
def gerar_sorteio(inicio, fim, quantidade):
    numerostotais = list(range(inicio, fim + 1))
    random.shuffle(numerostotais)
    numeros = numerostotais[:quantidade]
    return numeros
def sorteados(request):
    inicio = Numbers.objects.get().inicio
    fim = Numbers.objects.get().fim
    quantidade = Numbers.objects.get().quantidade
    if not request.session.get('numeros'):
        numeros = gerar_sorteio(inicio, fim, quantidade)
        request.session['numeros'] = numeros
    else:
        numeros = request.session['numeros']

    paginator = Paginator(numeros, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'lista': numeros
        }

    return render(request, "sortearprinci/sorteados.html", context)
def refresh(request):
    if request.session.get('numeros'):
        del request.session['numeros']
    return redirect('sorteados')