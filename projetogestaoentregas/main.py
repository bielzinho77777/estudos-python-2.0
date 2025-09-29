import os
import time
import json
from utils import pegarinformacoes, salvarinformacoes, pegarid
from motoristas import Motorista, listarmotoristas
from veiculo import Veiculo, listarveiculo
from entrega import Entrega, listarentregas, atualizar_status

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def checararquivos():
    arquivos = ["motorista", "veiculo", "entrega"]

    for nome in arquivos:
        caminho = os.path.join(BASE_DIR, f"{nome}.json")
        if not os.path.exists(caminho):  # só cria se não existir
            salvarinformacoes(nome, {})
            
def saindo():
    for i in range(0, 3):
        print(".", end="", flush=True)
        time.sleep(0.4)
    print()  # pula linha no final

def menu():
    checararquivos()
    while True:
        # limpar o terminal
        os.system("cls" if os.name == "nt" else "clear")

        print("=" * 50)
        print("        SISTEMA DE GERENCIAMENTO DE ENTREGAS")
        print("=" * 50)
        print("1 - Cadastrar motorista")
        print("2 - Cadastrar veículo")
        print("3 - Registrar entrega")
        print("4 - Atualizar status da entrega")
        print("5 - Listar entregas com filtro de status")
        print("6 - Listar todas as entregas")
        print("7 - Listar motoristas")
        print("8 - Listar veículos")
        print("0 - Sair")
        print("=" * 50)

        # pega a opção como string e tira os espaços
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            Motorista.cadastrar()

        elif opcao == "2":
            Veiculo.cadastrar()

        elif opcao == "3":
            Entrega.registrar_entrega()

        elif opcao == "4":
            print("\n" + "-" * 50)
            print("=== Atualizar Status da Entrega ===")
            print("-" * 50)
            atualizar_status()
            input("Pressione ENTER para continuar...")

        elif opcao == "5":
            filtro = input("Digite o status que deseja filtrar: ")
            print("\n" + "-" * 50)
            listarentregas(filtro=filtro)
            print("-" * 50)
            input("Pressione ENTER para continuar...")

        elif opcao == "6":
            print("\n" + "-" * 50)
            print("=== Listar Todas as Entregas ===")
            print("-" * 50)
            listarentregas()
            print("-" * 50)
            input("Pressione ENTER para continuar...")

        elif opcao == "7":
            print("\n" + "-" * 50)
            print("=== Listar motoristas ===")
            print("-" * 50)
            listarmotoristas()
            print("-" * 50)
            input("Pressione ENTER para continuar...")

        elif opcao == "8":
            print("\n" + "-" * 50)
            print("=== Listar Veículos ===")
            print("-" * 50)
            listarveiculo()
            print("-" * 50)
            input("Pressione ENTER para continuar...")
        elif opcao == "0":
            print("Saindo do programa", end="")
            saindo()
            break

        else:
            input("Opção inválida. Pressione ENTER para continuar...")


if __name__ == "__main__":
    menu()
