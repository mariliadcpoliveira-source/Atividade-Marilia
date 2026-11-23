Crie um decorador @medir_tempo que imprima quanto tempo uma função levou
para rodar e aplique-o a uma função recursiva otimizada com cache (lru_cache) 
para calcular Fibonacci.

-Resposta

import time
from functools import lru_cache

def medir_tempo(func):
    def wrapper(*args, **kwargs):
        inicio = time.perf_counter()
        resultado = func(*args, **kwargs)
        fim = time.perf_counter()
        print(f"Tempo de execução: {(fim - inicio) * 1000:.4f} ms")
        return resultado
    return wrapper

@lru_cache(maxsize=None)
def fib_otimizado(n):
    if n < 2:
        return n
    return fib_otimizado(n - 1) + fib_otimizado(n - 2)

@medir_tempo
def executar_fib(n):
    return fib_otimizado(n)

print(f"Resultado: {executar_fib(35)}")
