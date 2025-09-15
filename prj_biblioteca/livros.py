from autor import Autor
import json
from utils import verificar_maior_id
class Livro():
    #atributo da classe
    contador = 0
    def __init__(self, titulo, autor, genero, quantidade_estoque):
        Livro.contador= int(verificar_maior_id())+1
        self.id = str(Livro.contador)
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.quantidade_estoque = quantidade_estoque
        self.statusdisponivel = True 
        
    # antes de emprestar, fazemos a verificação se esta disponivel, se estiver, tiramos 1 do estoque.
    def pegar_livro(self):
        if self.statusdisponivel:
            remover_estoque(self.titulo)
            return f'livro {self.titulo} emprestado'
        else:
            return 'livro indisponivel'
    
    def devolver(self):
        self.quantidade_estoque += 1

    def checarstatus(self):
        if self.quantidade_estoque>=1:
            self.statusdisponivel = True 
            return True
        else:
            self.statusdisponivel = False 
            return False

    @staticmethod
    def remover_estoque(self, livro):
        self.quantidade_estoque -= 1
if __name__ == "__main__":
    l = Livro('')