from datetime import datetime

class Autor():
    contador = 0
    def __init__(self, nome, datanascimento):
        Autor.contador+=1
        self.id = str(Autor.contador)
        self.nome = nome
        self.datanascimento = datanascimento
        self.listalivrosautor = []
    def todict(self):
        return (str(self.id),{"nome" : self.nome, "datanascimento": self.datanascimento, "listalivrosautor": self.listalivrosautor})

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
    #MEXER DEPOIS
    return Autor('vovo', '17/12/1940')

if __name__ == "__main__":
    a = Autor('mamaco', '17/14/2009')
    print(a.transformar_data())