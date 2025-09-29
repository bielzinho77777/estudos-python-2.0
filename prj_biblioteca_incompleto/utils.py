import json

#funçao para obrigar a escolher o autor ja existente
#saber quantidade de livros iguais
def saber_quantidades():
    pass
def receber_informacoes_livro():
    with open("livros.json", "r", encoding="utf-8") as f:
        dados = json.load(f)
        return dados
def mandar_informacoes_livro(dados):
    with open("livros.json", "w", encoding="utf-8") as f:
        try:
            json.dump(dados, f, indent=4, ensure_ascii=False)
            return True
        except:
            return False
def adicionar_informacoes_livro(id, dados):
    recebido = receber_informacoes_livro()
    recebido[id] = dados

    if mandar_informacoes_livro(recebido):
        print("ok")
    else:
        print("erro")

#adicionar ao estoque de cada classe
#no caso a primeira variavel é pra saber qual classe é e depois coloca em sua determinada classe
def adicionar_ao_estoque(quem, objeto):
    if quem == "livros":
        id = objeto.id
        #titulo, autor, genero, statusdisponivel, numerodeemprestimos
        informacoes = {"titulo": objeto.titulo, "autor": {str(objeto.autor.id): objeto.autor.todict()}, "genero": objeto.genero, "quantidade_estoque": objeto.quantidade_estoque, "status_disponivel":objeto.checarstatus()}
        adicionar_informacoes_livro(id=id, dados=informacoes)
    elif quem == "autor":
        pass
    elif quem == "usuario":
        pass
    else: 
        input("Erro, chame um desenvolvedor")

#funçoes pra carregar o id
def verificar_maior_id(quem):
    if quem == "livro":
        dados = receber_informacoes_livro()
    elif quem == "autor":
        dados = receber_informacoes_autor()

    if dados:
        ids_existentes = []
        for ids in dados.keys():
            ids_existentes.append(ids)
        return max(ids_existentes)
    else:
        return 1


#AUTORRRRRRRRRR
def receber_informacoes_autor():
    with open("autor.json", "r", encoding="utf-8") as f:
        dados = json.load(f)
        return dados
def mandar_informacoes_autor(dados):
    with open("autor.json", "w", encoding="utf-8") as f:
        try:
            json.dump(dados, f, indent=4, ensure_ascii=False)
            return True
        except:
            return False
def adicionar_informacoes_autor(id, dados):
    recebido = receber_informacoes_autor()
    recebido[id] = dados

    if mandar_informacoes_autor(recebido):
        print("ok")
    else:
        print("erro")

def receber_e_verificar_data():
    while True:
        try:
            datanascimento = input("informe a data de nascimento do autor[dd/mm/aaaa]: ")
            datanascimento = datetime.strptime(datanascimento, "%d/%m/%Y").date()

        except ValueError:
            print('Data Inválida, digite novamente')

        else:
            return datanascimento
            break

if __name__ == "__main__":
    print(receber_informacoes_autor())

    adicionar_informacoes_autor()
    