from django.shortcuts import render, get_object_or_404, redirect
from . import forms
from .models import Produto, Categoria
from django.contrib import messages
from django.urls import reverse_lazy
# Create your views here.
def index(request, tipocategoria = None):
    categorias = Categoria.objects.all()
    if not tipocategoria:
        objetos = Produto.objects.all()
    else:
        objetos = Produto.objects.filter(categoria__nome = tipocategoria)
        
    context = {"produtos": objetos, "categorias": categorias}
    return render(request, "main/index.html", context)
def adicionar_produto(request):
    if request.method == "POST":
        form = forms.ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('index'))
    else:
        form = forms.ProdutoForm()
    return render(request, "main/adicionar.html", {"form": form})

def detalhes_produto(request, id):
    objetos = get_object_or_404(Produto, id=id)
    context = {"objeto": objetos}
    return render(request, "main/detalhes.html", context)

def excluir_produto(request, id):
    objetos = get_object_or_404(Produto, id=id)
    objetos.delete()
    
    return redirect('index')