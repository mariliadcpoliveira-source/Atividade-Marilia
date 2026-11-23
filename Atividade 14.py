Escreva uma função que determine se duas strings são anagramas uma da outra
(possuem exatamente as mesmas letras).

-Resposta 

def sao_anagramas(s1, s2):
    s1_limpa = sorted(s1.replace(" ", "").lower())
    s2_limpa = sorted(s2.replace(" ", "").lower())
    return s1_limpa == s2_limpa

print(sao_anagramas("amor", "roma"))  # True
print(sao_anagramas("python", "java"))  # False
