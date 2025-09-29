import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Define o caminho para o JSON na mesma pasta
caminho_arquivo = os.path.join(BASE_DIR, "entregas.json")

def pegarid(arquivo):
    dados = pegarinformacoes(arquivo)

    if not dados:
        return 0
    
    l = []

    for j,k in dados.items(): 
        l.append(int(j))
    return max(l)

def pegarinformacoes(arquivo):
    caminho_arquivo = os.path.join(BASE_DIR, f"{arquivo}.json")

    if os.path.exists(caminho_arquivo):
        with open(caminho_arquivo, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def salvarinformacoes(arquivo, dados):
    caminho_arquivo = os.path.join(BASE_DIR, f"{arquivo}.json")
    dados_existentes = {}

    if os.path.exists(caminho_arquivo):
        with open(caminho_arquivo, "r", encoding="utf-8") as f:
            dados_existentes = json.load(f)
    dados_existentes.update(dados)
    
    with open(caminho_arquivo, "w", encoding="utf-8") as f:
        json.dump(dados_existentes, f, indent=4)
    # print(dados)
    return True

#PARA TESTES
if __name__ == "__main__":
    pass