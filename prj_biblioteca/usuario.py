from livros import Livro
from utils import receber_informacoes_livro
class Usuario():
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
        self.historico_de_emprestimos = []

    def pegar_livro(self, titulo):
        if verificar_livro(titulo):
            return f'livro {titulo} pego!'
        else:
            return f'livro {titulo} indisponivel'

def verificar_livro(titulo):
    dados = receber_informacoes_livro()
    for i in dados:
        for k,v in dados[i].items():
            if k == 'titulo':
                if v == titulo:
                    return True

if __name__ == '__main__':
    a = Usuario('alanbida', 'alanbida@example.com')    
    print(a.pegar_livro('pc'))