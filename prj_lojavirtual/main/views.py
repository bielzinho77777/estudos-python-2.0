from django.shortcuts import render,redirect, get_object_or_404
from django.views.generic.edit import FormView
from main import forms
from django.urls import reverse_lazy
from .models import Categoria, Produto
from carrinho.forms import FormAdicionarProdutoAoCarrinho

# Create your views here.
class View_FaleConosco(FormView):
    template_name = 'fale_conosco.html'
    form_class = forms.FormFaleConosco
    success_url = reverse_lazy('fale_conosco')
    def form_valid(self, form):
        form.enviar_mensagem_por_email()
        return super().form_valid(form)
    
def lista_produtos(request,slug_categoria=None):
    categoria = None
    lista_categorias = Categoria.objects.all()
    lista_produtos = Produto.objects.filter(disponivel=True)
    if slug_categoria:
        categoria = get_object_or_404(Categoria, slug=slug_categoria)
        lista_produtos = lista_produtos.filter(categoria=categoria)
    contexto = {'categoria':categoria,'lista_produtos':lista_produtos,'lista_categorias':lista_categorias}
    return render(request,'produtos/listar.html',contexto)
def detalhes_produto(request, id, slug_produto):
    produto = get_object_or_404(Produto, id=id, slug=slug_produto, disponivel=True)
    form = FormAdicionarProdutoAoCarrinho()
    contexto = {'produto':produto, 'form_produto_carrinho':form}
    return render(request,'produtos/detalhes.html',contexto)


def fale_conosco(request):
    if request.method == 'POST':
        form = forms.FaleConoscoForm(request.POST)
        if form.is_valid():
            form.enviar_mensagem_por_email()
            return redirect('index') 
    else:
        form = forms.FaleConoscoForm()
    return render(request, 'fale_conosco.html', {'form': form})
