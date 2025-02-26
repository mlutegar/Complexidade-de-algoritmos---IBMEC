# busca simples em uma lista de inteiros

def busca_simples(array, valor):
    for i in range(len(array)):
        if array[i] == valor:
            return i
    return -1

# Complexidade de tempo: O(n)
# Explicação: O(n) pois, no pior caso, o loop percorre todos os elementos do array antes de encontrar o valor ou concluir que ele não está presente.
