from utils import pegarid, salvarinformacoes, pegarinformacoes
import re

class Veiculo():
    idcont = 1

    def __init__(self, placa, modelo):
        Veiculo.idcont = int(pegarid("veiculo")) + 1
        self.id = Veiculo.idcont
        self.placa = placa
        self.modelo = modelo

    def __str__(self):
        return f"{self.id} - {self.modelo} - Placa: {self.placa}"
    
    def todict(self):
        return {f"{str(self.id)}": {"modelo": self.modelo, "placa": self.placa}}
    
    @staticmethod
    def toobj(dicionario):
        return Veiculo(dicionario["placa"], dicionario["modelo"])
    
    @staticmethod
    def validando(placa):
        antigo = r"^[A-Z]{3}[0-9]{4}$"
        mercosul = r"^[A-Z]{3}[0-9][A-Z][0-9]{2}$"
        return bool(re.match(antigo, placa.upper()) or re.match(mercosul, placa.upper()))
    
    @staticmethod
    def cadastrar():
        veiculos = pegarinformacoes("veiculo")
        modelo = input("Modelo do veículo: ")

        while True:
            placa = input("Placa do veículo: ").upper()

            if Veiculo.validando(placa):
                veiculos = pegarinformacoes("veiculo")

                if not veiculos:
                    veiculos = {}

                novoid = pegarid("veiculo") + 1
                v = Veiculo(placa, modelo)
                v.id = novoid

                veiculos[str(v.id)] = {"modelo": v.modelo, "placa": v.placa}
                salvarinformacoes("veiculo", veiculos)

                print("-" * 50)
                print("==== VEÍCULO CADASTRADO COM SUCESSO ====")
                print("-" * 50)
                input("Pressione ENTER para continuar...")
                
                break
            else:
                print("-" * 50)
                print("[ERRO] Placa inválida!")
                print("-" * 50)
def listarveiculo():
    veiculos = pegarinformacoes("veiculo")

    if not veiculos:
        print("Nenhum veículo cadastrado!")
        return False
    
    else:
        for i in range(len(veiculos)):
            print(f"{i+1} - {veiculos[str(i+1)]['placa']} - {veiculos[str(i+1)]['modelo']}")