
Crie uma função que receba um número inteiro e retorne True se ele for 
primo e False caso contrário.

-Resposta

def eh_primo(n):
  if n < 2:
    return False 
  for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
      return False 
  return True

print(eh_primo(29)) #True
print(eh_primo(15)) # False
