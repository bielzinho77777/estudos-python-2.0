from datetime import datetime
from utils import adicionar_informacoes_autor,verificar_maior_id, receber_informacoes_autor
class Autor():
    contador = 0
    def __init__(self, nome, datanascimento):
        Autor.contador= int(verificar_maior_id("autor"))+1
        self.id = str(Autor.contador)
        self.nome = nome
        self.datanascimento = datanascimento
        self.listalivrosautor = []
    def todict(self):
        return {"nome" : self.nome, "datanascimento": self.datanascimento, "listalivrosautor": self.listalivrosautor}

    def transformar_data(self):
        try:
            self.datanascimento = datetime.strptime(self.datanascimento, "%d/%m/%Y").date()
            return self.datanascimento
        
        except ValueError:
            print( 'data de nascimento invalida')
            self.datanascimento = datetime.strptime("01/01/2000", "%d/%m/%Y").date()
            return (self.datanascimento)


    def adicionar_livro(self, titulo, genero, quantidade):
        self.listalivrosautor.append([titulo, genero, quantidade])
def escolher_autor():
    dados = receber_informacoes_autor()
    if not dados:
        return "vazio"
    l = []
    for k, i in dados.items():
        l.append(i["nome"])
    for j in l:
        print(f"{j}", end=", ")
    while True:
        autor = input("\nInforme qual é o autor do livro (se nao tiver nessa lista cadastre novos autores e digite exit para sair): ").lower()
        l = [b.lower() for b in l]
        if autor == "exit":
            return False
        elif autor in l:
            for a in range(len(l)):
                if l[a] == autor:
                    for k,i in dados.items():
                        if i["nome"] == l[a]:
                            aut = Autor(dados[k]["nome"], dados[k]["datanascimento"])
                            return aut
                    return l[a]
        else:
            input("Erro, o autor nao existe na lista. Pressione enter para continuar")

if __name__ == "__main__":
    a = Autor('mamaco', '17/14/2009')
    escolher_autor()