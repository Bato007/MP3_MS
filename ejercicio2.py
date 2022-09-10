import matplotlib.pyplot as plt
import random

# VARIABLE ALEATORIA: NUMERO DE CARAS AL TIRAR 3 MONEDAS DE UNA MONEDA JUSTA
probability_distribution = {
  0: 1/8,
  1: 4/8,
  2: 7/8,
  3: 1,
}

def generate_values(n, pmf):
  values = []
  for _ in range(n):
    u_random = random.uniform(0, 1)
    print('===============================================')
    for i in pmf:
      print('VALUE: ', pmf[i], 'RANDOM: ', u_random)
      if (u_random <= pmf[i]):
        values.append(pmf[i])
        break
  print(values)
  
  plt.title('Ejercicio 2')
  plt.xlabel('Probabilidad')
  plt.ylabel('Total de eventos')
  plt.hist(values, color='#369399')
  plt.show()


generate_values(100, probability_distribution)

