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
  # Se genera un arreglo vacio para meter los valores generados
  values = []
  for _ in range(n):
    # Se genera un numero aleatorio entre 0 y 1
    u_random = random.uniform(0, 1)
    print('===============================================')
    # Se revisa a que probabilidad corresponde
    for i in pmf:
      print('VALUE: ', pmf[i], 'RANDOM: ', u_random)
      if (u_random <= pmf[i]):
        # Se agrega el valor correpondiente al arreglo de valores
        values.append(pmf[i])
        break
  print(values)
  
  # Grafica
  plt.title('Ejercicio 2')
  plt.xlabel('Probabilidad')
  plt.ylabel('Total de eventos')
  plt.hist(values, color='#369399')
  plt.show()


generate_values(100, probability_distribution)

