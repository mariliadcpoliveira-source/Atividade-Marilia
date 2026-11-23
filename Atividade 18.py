Dada uma string contendo (), [] e {}, verifique se os símbolos estão
corretamente abertos e fechados na ordem certa.

-Resposta

def validar_parenteses(s):
    pilha = []
    mapa = {")": "(", "]": "[", "}": "{"}
    for char in s:
        if char in mapa.values():
            pilha.append(char)
        elif char in mapa:
            if not pilha or pilha.pop() != mapa[char]:
                return False
    return len(pilha) == 0

print(validar_parenteses("{[()]}"))  # True
print(validar_parenteses("{[(])}"))  # False
