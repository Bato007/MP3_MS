'''
  Para poder correr esta condigo es necesario correr los sieguientes comandos:
    - pip install numpy
    - pip install numpy_financial
'''
import numpy as np
import numpy_financial as npf

# Valores para simular el flujo de la variable normal
mallValues = [
  (-600, 50),
  (-200, 50),
  (-600, 100),
  (250, 150),
  (350, 150),
  (400, 150)
]
hotelValues = [
  (-800, 50),
  (-800, 100),
  (-700, 150),
  (300, 200),
  (400, 200),
  (500, 200),
]

# Simulando el flujo normal
def simulate(initialValue, values, low, high):
  array = [initialValue]
  for value in values:
    array.append(np.random.normal(loc=value[0], scale=value[1], size=1)[0])

  array.append(np.random.uniform(low=low, high=high, size=1)[0])
  return array

iterations=100
vpnMall = []
vpnHotel = []
vpn = 0.1

for _ in range(iterations):
  # Flujo Mall ----------------------------------------
  mallSimulation = simulate(
    initialValue=-900,
    values=mallValues,
    low=1600,
    high=6000
  )

  vpnMall.append(npf.npv(vpn, mallSimulation))

  # Flujo Hotel ---------------------------------------
  hotelSimulation = simulate(
    initialValue=-800,
    values=hotelValues,
    low=2000,
    high=8440
  )

  vpnHotel.append(npf.npv(vpn, hotelSimulation))

# Estadisticas
vpnMeanMall = np.mean(vpnMall)
vpnStdMall = np.std(vpnMall)

vpnMeanHotel = np.mean(vpnHotel)
vpnStdHotel = np.std(vpnHotel)

# Mostrando resultados
print('\n========== Iteraciones:', str(iterations), '==========')
print('Valores del Mall')
print('Promedio:', round(float(vpnMeanMall), 2))
print('Desviacion Estandar:', round(float(vpnStdMall), 2))
print('Rango: [' + str(round(float((vpnMeanMall - vpnStdMall)), 2)), '->', 
  str(round(float((vpnMeanMall + vpnStdMall)), 2)) + ']')

print('\nValores del hotel')
print('Promedio:', round(float(vpnMeanHotel), 2))
print('Desviacion Estandar:', round(float(vpnStdHotel), 2))
print('Rango: [' + str(round(float((vpnMeanHotel - vpnStdHotel)), 2)), '->', 
  str(round(float((vpnMeanHotel + vpnStdHotel)), 2)) + ']\n')
