from autor import Autor,escolher_autor
from livros import Livros
from datetime import datetime
import json

class Emprestimo:
    def __init__(self, usuario, livro, data_emprestimo, data_devolucao=None):
        self.usuario = usuario
        self.livro = livro
        self.data_emprestimo = data_emprestimo
        self.data_devolucao = data_devolucao

    def finalizar_emprestimo(self):
        self.data_devolucao = datetime.now()
        return self.__dict__()

    def to_json(self):
        return json.dumps(self.finalizar_emprestimo(), indent=4, cls=EmprestimoEncoder)

    def __dict__(self):
        return {
            'usuario': self.usuario,
            'livro': self.livro,
            'data_emprestimo': self.data_emprestimo,
            'data_devolucao': self.data_devolucao
        }


class EmprestimoEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Emprestimo):
            return {
                'usuario': obj.usuario,
                'livro': obj.livro,
                'data_emprestimo': obj.data_emprestimo,
                'data_devolucao': obj.data_devolucao
            }
        return super().default(obj)