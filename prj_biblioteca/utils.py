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
        informacoes = {"titulo": objeto.titulo, "autor": {objeto.autor.todict()[0]: objeto.autor.todict()[1]}, "genero": objeto.genero, "quantidade_estoque": objeto.quantidade_estoque, "status_disponivel":objeto.checarstatus()}
        adicionar_informacoes_livro(id=id, dados=informacoes)
    elif quem == "autor":
        pass
    elif quem == "usuario":
        pass
    else: 
        input("Erro, chame um desenvolvedor")

#funçoes pra carregar o id
def verificar_maior_id():
    dados = receber_informacoes_livro()

    if dados:
        ids_existentes = []
        for ids in dados.keys():
            ids_existentes.append(ids)
            print(ids)
        return max(ids_existentes)
    else:
        return 1

if __name__ == "__main__":

    print(adicionar_ao_estoque("livros", l1))
    print(adicionar_ao_estoque("livros", l2))
