from decimal import Decimal
from django.conf import settings
from main.models import Produto

class Carrinho:
    def __init__(self, request):
        self.__session = request.session
        carrinho = self.__session.get(settings.ID_CARRINHO)
        if not carrinho:
            carrinho = self.__session[settings.ID_CARRINHO] = {}
        self.__carrinho = carrinho
    
    def adicionar(self, produto,quantidade=1, atualizar_quantidade=False):
        id_produto = str(produto.id)
        if id_produto not in self.__carrinho:
            self.__carrinho[id_produto] = {'quantidade':0,'preco':str(produto.preco)}
        if atualizar_quantidade:
            self.__carrinho[id_produto]['quantidade'] = quantidade
        else:
            self.__carrinho[id_produto]['quantidade'] += quantidade
        self.__salvar()

    def __salvar(self):
        self.__session[settings.ID_CARRINHO] = self.__carrinho
        self.__session.modified = True
    
    def remover(self, produto):
        id_produto = str(produto.id)
        if id_produto in self.__carrinho:
            del self.__carrinho[id_produto]
            self.__salvar()

    def __iter__(self):
        ids_produtos = self.__carrinho.keys()
        produtos = Produto.objects.filter(id__in=ids_produtos)
        carrinho = self.__carrinho.copy()
        for produto in produtos:
            carrinho[str(produto.id)]['produto'] = produto
        for item in carrinho.values():
            item['preco'] = Decimal(item['preco'])
            item['total'] = item['preco'] * item['quantidade']
            yield item

    def __len__(self):
        resultado = 0
        for item in self.__carrinho.values():
            resultado += item['quantidade']
        return resultado
    
    def get_total_geral(self):
        resultado = Decimal('0.0')
        for item in self.__carrinho.values():
            subtotal = Decimal(item['preco']) * Decimal(item['quantidade'])
            resultado += subtotal
        return resultado
    
    def limpar_carrinho(self):
        if settings.ID_CARRINHO in self.__session:
            del self.__session[settings.ID_CARRINHO]
            self.__session.modified = True
