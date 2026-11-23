Dada uma lista de números, crie uma única linha usando 
list comprehension que retorne o quadrado apenas dos números pares maiores que 10.

-Resposta

numeros = [4, 12, 7, 15, 20, 8, 14]
resultado = [x**2 for x in numeros if x % 2 == 0 and x > 10]
print(resultado)  # [144, 400, 196]
