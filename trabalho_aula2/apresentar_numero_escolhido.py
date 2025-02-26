# apresentar um número escolhido aleatoriamente usando random

import random

def apresentar_numero_escolhido():
    numero = random.randint(1, 100)
    print(f'O número escolhido foi: {numero}')

# Complexidade de tempo: O(1)
# Explicação: O(1) pois a função random.randint() é executada uma vez
