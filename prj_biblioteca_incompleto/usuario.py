from livros import Livro
from utils import receber_informacoes_livro
import json

class Usuario():
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
        self.historico_de_emprestimos = []

    def pegar_livro(self, titulo, caminho="livros.json"):    
        if verificar_livro(titulo):
            with open(caminho, 'r', encoding='utf-8') as arquivo:
                livros = json.load(arquivo)

            for id_livro, dados in livros.items():
                if dados['titulo'].lower() == titulo.lower():
                    self.id_livro_pego = id_livro # guarda o ID como string
                    dados['quantidade_estoque'] -= 1
                    #atualizar_json(id)

            return f'livro {titulo} pego!'
            a.adicionar_historico(titulo, self.id_livro_pego)
        else:
            return f'livro {titulo} indisponivel'

    def adicionar_historico(self, titulo, id):
        self.historico_de_emprestimos.append((titulo, id))
        print(self.historico_de_emprestimos)

    def devolver_livro(self, titulo, caminho="livros.json"):
        try:
            with open(caminho, 'r', encoding='utf-8') as arquivo:
                livros = json.load(arquivo)
            if not livros:
                print("vazil")
            else:
                for id_livro, dados in livros.items():
                    print(dados['titulo'])
                    if dados['titulo'].lower() == titulo.lower():
                        dados['quantidade_estoque'] += 1
                        print(dados)
                        #atualizar_json(id)
        except:
            print('Erro chame um dev')
                

def verificar_livro(titulo):
    dados = receber_informacoes_livro()
    for i in dados:
        for k,v in dados[i].items():
            if k == 'titulo':
                if v == titulo:
                    return True


if __name__ == '__main__':
    a = Usuario('junior', 'junior@example.com')    
    a.devolver_livro('pc')