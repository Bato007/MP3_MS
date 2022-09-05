import matplotlib.pyplot as plt
import random

# VARIABLE ALEATORIA: NUMERO DE CARAS AL TIRAR 3 MONEDAS DE UNA MONEDA JUSTA
probability_distribution = {
  0: 1/8,
  1: 3/8,
  2: 3/8,
  3: 1/8,
}

def generate_values(n, pmf):
  values = []
  for _ in range(n):
    number_of_heads = random.randint(0, 3)
    probability = pmf[number_of_heads]
    values.append(probability)
  
  plt.title('Ejercicio 2')
  plt.xlabel('Probabilidad')
  plt.ylabel('Total de eventos')
  plt.hist(values, color='#369399')
  plt.show()


generate_values(100, probability_distribution)

