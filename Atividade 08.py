Calcule o fatorial de um número inteiro positivo
(ex: 5! = 5 * 4 * 3 * 2 * 1 = 120).

-Resposta

n = int(input("Número para calcular o fatorial: "))
fatorial = 1 
for i in range(1, n + 1):
  fatorial *= i
print(f"{n}! = {fatorial}")
