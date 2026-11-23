Dada uma lista com elementos repetidos, retorne uma nova lista
sem duplicatas preservando a ordem original.

-Resposta

def remover_duplicatas(lista):
    vistos = set()
    resultado  = []
    for item in lista:
      if item not in vistos:
        vistos.add(item)
        resultado.append(item)
    return resultado 
print(remover_duplicatas([1, 2, 2, 3, 4, 3, 5, 1]))
