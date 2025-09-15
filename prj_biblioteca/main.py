from autor import Autor,escolher_autor
from utils import adicionar_ao_estoque
from livros import Livro
def mostrar_menu():
    print("="*30)
    print("   SISTEMA DE BIBLIOTECA")
    print("="*30)
    print("1) Cadastrar novo livro")
    print("2) Cadastrar novo autor")
    print("3) Cadastrar novo usuário")
    print("4) Registrar empréstimo")
    print("5) Registrar devolução")
    print("6) Buscar livros")
    print("7) Buscar usuários")
    print("8) Ver estatísticas")
    print("9) Sair")
    print()

def main():
    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("Função de cadastrar livro")
            titulo = input("Informe o titulo do livro: ")
            autor= escolher_autor()
            genero = input("informe o genero do livro: ")
            estoque = int(input("Informe o estoque: "))
            while not estoque>=1:
                estoque = int(input("ERRO, ESTOQUE DEVE SER MAIOR QUE 0: "))
        
            adicionar_ao_estoque("livros", Livro(titulo, autor, genero, estoque))
            print("Livro adicionado com sucesso")
            input("Pressione enter para continuar")
            
            # chamar função de cadastro de livro aqui
        elif opcao == "2":
            print("Função de cadastrar autor")
            nome_autor = input("informe o nome do autor: ")
            datanascimento_autor = input("informe a data de nascimento do autor[dd/mm/aaaa]: ")
            # chamar função de cadastro de autor aqui
        elif opcao == "3":
            print("Função de cadastrar usuário")
            # chamar função de cadastro de usuário aqui
        elif opcao == "4":
            print("Função de registrar empréstimo")
        elif opcao == "5":
            print("Função de registrar devolução")
        elif opcao == "6":
            print("Função de buscar livros")
        elif opcao == "7":
            print("Função de buscar usuários")
        elif opcao == "8":
            print("Função de ver estatísticas")
        elif opcao == "9":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida! Tente novamente.")
        print()  # linha em branco para melhorar visualização

if __name__ == "__main__":
    main()
