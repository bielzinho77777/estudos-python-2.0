from autor import Autor,escolher_autor
from utils import adicionar_ao_estoque, adicionar_informacoes_autor,receber_e_verificar_data
from livros import Livro
def mostrar_menu():
    print("="*30)
    print("   SISTEMA DE BIBLIOTECA")
    print("="*30)
    print("1) Cadastrar novo livro")
    print("2) Cadastrar novo autor")
    print("3) Registrar empréstimo")
    print("4) Registrar devolução")
    print("5) Buscar livros")
    print("6) Buscar usuários")
    print("7) Ver estatísticas")
    print("8) Sair")
    print()

def main():
    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1": #FEITO
            print("Função de cadastrar livro")
            
            titulo = input("Informe o titulo do livro: ")
            autor =escolher_autor()
            if autor =="N":
                print("A lista de autores esta vazia, pressione enter para continuar:")
                continue
            if autor== False:
                continue
        
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
            datanascimento_autor = receber_e_verificar_data()
            a1 = Autor(nome_autor, datanascimento_autor)
            dic = a1.todict()
            try:
                adicionar_informacoes_autor(a1.id, dic)
                input(dic)
            except:
                input("Houve um erro ao adicionar, informe um desenvolvedor\nPressione enter para continuar")
            # chamar função de cadastro de autor aqui
        elif opcao == "3":
            print("Função de registrar empréstimo")
            # chamar função de cadastro de usuário aqui
        elif opcao == "4":
            print("Função de registrar devolução")
        elif opcao == "5":
            print("Função de buscar livros")
        elif opcao == "6":
            print("Função de buscar usuários")
        elif opcao == "7":
            print("Função de ver estatísticas")

            
        elif opcao == "8":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida! Tente novamente.")
        print()  # linha em branco para melhorar visualização

if __name__ == "__main__":
    main()
