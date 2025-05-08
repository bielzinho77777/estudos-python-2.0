import time
import random
import os
#nao vou chamar em algum banco de dados ou json pq é meio chato
#PLURAL LISTA, SINGULAR VARIAVEL
contas = []
numeros = []
senhas = []
class Conta:
    def __init__(self,numero, titular, saldo, limite, senha):
        self.senha = senha
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        #talvez seja uma variavel desnecessaria, mas fiz pra ter um codigo mais limpo e seguro
        self.maximosaque = self.saldo+self.limite

    def depositar(self,depositado):
        if depositado >0:
            self.saldo += depositado
            self.maximosaque = self.saldo+self.limite
            print("Depositando\nAguarde",end="")
            for i in range(3):
                print(".", end="", flush=True)
                time.sleep(1.5)
            print()
            print(f"Valor depositado com sucesso, no valor de R${depositado}")
            input("Pressione enter para continuar")
        else:
            print(f"Valor incorreto para ser depositado")
    def sacar(self,valor_sacado):
        if valor_sacado > self.maximosaque:
            print("Saldo insuficiente para saque")
            input("Pressione enter para continuar. ")
        else:
            print("Sacando\nAguarde",end="")
            self.saldo -= valor_sacado
            self.maximosaque = self.saldo+self.limite
            for i in range(3):
                print(".", end="", flush=True)
                time.sleep(1.5)
            print()
            print(f"O valor R${valor_sacado} foi sacado com sucesso")
    def extrair_saldo(self):
        print(f"O saldo de {self.titular} é de {self.saldo} reais")
        input("Pressione enter para continuar. ")

def aguardar(tempo):
    print("Aguarde",end="")
    for i in range(3):
        print(".", end="", flush=True)
        time.sleep(tempo)
    print()
def depoislogin(contausada):
    while True:
        os.system("cls")
        fazer = 4
        while fazer <0 or fazer>3:
            print('='*50)
            print("Informe a operação que deseja realizar:")
            print('='*50,'\n\n') 
            fazer = int(input(f"[0]Depositar\n[1]Sacar\n[2]Extrair saldo\n[3]Sair\n"))
        if fazer ==0:
            depositado = float(input("Informe o valor a ser depositado: "))
            if depositado<0:
                print("Não pode depositar nada negativo")
                input("pressione enter para continuar")
            else:
                contausada.depositar(depositado)
        elif fazer ==1:
            sacado = float(input("Informe o valor que sera sacado: "))
            contausada.sacar(sacado)
        elif fazer ==2:
            contausada.extrair_saldo()
        elif fazer ==3:
            break

while True:
    os.system("cls")
    verificar = 5
    while verificar <0 or verificar>4:
        print('='*50)
        print("Informe a operação que deseja realizar:")
        print('='*50,'\n\n')
        verificar = int(input(f"[0] Cadastar conta\n[1]Efetuar login\n[2]Verificar numeros das contas existentes\n[3]Deletar conta\n[4]Sair\n"))
    if verificar ==0:
        while True:
            #numero, titular, saldo, limite, senha
            titular = input("Informe o nome do dono da conta: ")
            saldo = 0
            limite = 1000
            #Nao vou fazer negocio de esquecer senha ou confirmar, para fins educativos nao é necessario
            senha = input("Informe a senha: ")
            aguardar(0.5)
            if senha in senhas:
                print("[ERRO], essa senha nao pode ser cadastrada")
            elif len(senha)<=3:
                print("[ERRO] Senha muito pequena")
            else:
                break
        while True:
            numero = ''
            for i in range(4):
                x = random.randint(0,9)
                numero+=str(x)
            if numero not in numeros:
                numero = int(numero)
                break
        conta1 = Conta(numero=numero,titular=titular, saldo=saldo, limite=limite, senha=senha)
        contas.append(conta1)
        numeros.append(numero)
        senhas.append(senha)
        print("Cadastrado com sucesso")
        input(f"Sua conta foi cadastada com o numero {numero}, não se esqueça\npressione enter pra continuar:")

        
    elif verificar ==2:
        aguardar(0.35)
        if numeros == []:
            print("Nenhuma conta existente!")
        else:
            print(numeros)
        input("pressione enter pra continuar. ")

    elif verificar == 3:
        deletar = int(input("Informe o número da conta que deseja deletar: "))
        aguardar(0.35)
        if deletar not in numeros:
            print("Esse numero nao esta cadastrado")
            input("Pressione enter para continuar. ")
        else:
            numeros.remove(deletar)
            for i in contas:
                if i.numero == deletar:
                    senharemo = i.senha
                    contaremo = i
                    break
            senhas.remove(senharemo)
            contas.remove(contaremo)
            input(f"conta deletada com sucesso\nPressione enter para continuar. ")
            
    elif verificar ==1:
        login = int(input("Informe o número da conta: "))
        aguardar(0.35)
        if login not in numeros:
            print("Esse numero nao esta registrado")
            time.sleep(2)
        else:
            senhadigi = input(f"Informe a senha da conta {login}: ")
            aguardar(0.35)
            for i in contas:
                if i.numero==login:
                    contausada = i
                    break
            if senhadigi!= contausada.senha:
                print("[ERRO] Senha errada")
                input("Pressione enter para continuar. ")
            else:
                depoislogin(contausada=contausada)
    elif verificar ==4:
        break


print(contas)
print(numeros)
print(senhas)