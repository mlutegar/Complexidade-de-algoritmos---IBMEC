# duplicar valores de uma array

def duplicar_valores(array):
    for i in range(len(array)):
        array[i] = array[i] * 2
    return array

# Complexidade de tempo: O(n)
# Explicação: O loop percorre todos os elementos do array uma única vez,
# realizando uma multiplicação e atribuição para cada um, resultando em complexidade linear.
