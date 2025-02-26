# Calcular o fatorial de um número utilizando recursividade

def calcular_fatorial(numero):
    if numero == 0:
        return 1
    return numero * calcular_fatorial(numero - 1)

# Complexidade de tempo: O(n)
# Explicação: O(n) pois a função é chamada n vezes, onde n é o número escolhido