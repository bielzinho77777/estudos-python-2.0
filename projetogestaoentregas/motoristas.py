from utils import pegarinformacoes, salvarinformacoes, pegarid

class Motorista():
    idcont = 1

    def __init__(self, nome: str, cnh: str):
        Motorista.idcont = int(pegarid("motorista")) + 1
        self.id = Motorista.idcont
        self.nome = nome
        self.cnh = cnh
        
    def todict(self):
        return {f"{str(self.id)}": {"nome": self.nome, "cnh": self.cnh}}
    
    @staticmethod
    def toobj(dicionario):
        return Motorista(dicionario["nome"], dicionario["cnh"])

    def __str__(self):
        return f"{self.id} - {self.nome} - {self.cnh}"

    @staticmethod
    def valida_cnh(cnh):
        return cnh.isdigit() and len(cnh) == 11
    
    @staticmethod
    def cadastrar():
        motoristas = pegarinformacoes("motorista")
        nome = input("Nome do motorista: ")

        while True:
            cnh = input("CNH (11 dígitos): ")
            if Motorista.valida_cnh(cnh):
                novo_id = pegarid("motorista") + 1
                m = Motorista(nome, cnh)
                m.id = novo_id

                motoristas[str(m.id)] = {"nome": m.nome, "cnh": m.cnh}
                salvarinformacoes("motorista", motoristas)

                print("-" * 50)
                print("==== MOTORISTA CADASTRADO COM SUCESSO ====")
                print("-" * 50)
                break
            else:
                print("-" * 50)
                print("[ERRO] CNH INVÁLIDA!")
                print("-" * 50)

def listarmotoristas():
    motoristas = pegarinformacoes("motorista")

    if not motoristas:
        print("Nenhum motorista cadastrado!")
        return False

    else:
        for i in range(len(motoristas)):
            print(f"{i+1} - {motoristas[str(i+1)]['nome']} - {motoristas[str(i+1)]['cnh']}")
if __name__ == "__main__":
    e = Motorista("", "")
    print("-" * 50)
    print(e)
    print("-" * 50)
