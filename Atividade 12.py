Receba um texto e retorne um dicionário onde as chaves 
são as palavras e os valores são a quantidade de vezes que cada uma aparece.

-Resposta

def contar_palavras(texto):
  palavras = texto.lower().split()
  contagem = {}
  for p in palavras:
    contagemm[p] = contagem.get(p, 0) + 1
  return contagem
print(contar_palavras("python é legal e python é poderoso")
