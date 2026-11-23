Implemente uma função que criptografe uma mensagem deslocando
cada letra do alfabeto por um número K de posições.

-Resposta

def cifra_cesar(texto, deslocamento):
    resultado = ""
    for char in texto:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            novo_char = chr((ord(char) - base + deslocamento) % 26 + base)
            resultado += novo_char
        else:
            resultado += char
    return resultado

print(cifra_cesar("Python 3.12!", 3)) 
