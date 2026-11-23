COnte quantas vogais existem em uma frase digitada pelo usuário
(desconsidere acentos).

-Resposta

frase = input("Digite uma frase: ").lower()w
vogais = "aeioou"
contador = sum(1 for letra in frase if letra in vogais)
print(f"Total de vogais: {contador}")
