# verificar se um número é primo

def verificar_numero_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return

# Complexidade de tempo: O(n)
# Explicação: O(n) pois o loop for percorre todos os números de 2 até o número escolhido