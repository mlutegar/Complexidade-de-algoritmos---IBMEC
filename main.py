import time
from fib_recursive import fib_recursive
from fib_memo import fib_memo
from fib_matrix import fib_matrix


def medir_tempo(func, n):
    start_time = time.time()
    result = func(n)
    end_time = time.time()
    return result, end_time - start_time


def testar_valores_fixos(func, nome_func):
    for n in [10, 100]:
        result, exec_time = medir_tempo(func, n)
        print(f"[{nome_func}] F({n}) = {result} | Tempo: {exec_time:.6f}s")


def encontrar_limite(func, nome_func, tempo=10):
    n = 1
    start_time = time.time()

    while time.time() - start_time < tempo:
        result = func(n)
        n += 1

    print(f"\n[{nome_func}] Maior F(n) calculado em {tempo} segundos: F({n - 1})")


print("\n=== Teste de Limite de 1 Minuto ===")
encontrar_limite(fib_memo, "Memorização")
encontrar_limite(fib_matrix, "Matriz")
encontrar_limite(fib_recursive, "Recursivo")

print("\n=== Teste com F(10) e F(100) ===")
testar_valores_fixos(fib_recursive, "Recursivo")  # Remova se quiser evitar lentidão
testar_valores_fixos(fib_memo, "Memorização")
testar_valores_fixos(fib_matrix, "Matriz")


