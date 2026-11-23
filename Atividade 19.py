Implemente o algoritmo de busca binária para encontrar o índice 
de um elemento em uma lista ordenada (retorne -1 se não encontrar).

-Resposta

def busca_binaria(lista, alvo):
    esquerda, direita = 0, len(lista) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if lista[meio] == alvo:
            return meio
        elif lista[meio] < alvo:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return -1

dados = [2, 5, 8, 12, 16, 23, 38, 56, 72]
print(busca_binaria(dados, 23))  # 5
