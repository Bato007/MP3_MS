import numpy as np
from random import random

X = [
  (0.4, 10),
  (0.3, 9),
  (0.3, 11),
]

# Se obtiene la cantidad de periodicos que se venden ese dia 
def getDemand(X):
  rValue = random()
  acumulated = 0
  newspapers = 0
  for x in X:
    if (rValue < x[0] + acumulated):
      newspapers = x[1]
      break
    else:
      acumulated += x[0]
  return newspapers

iterations = 3650
offer = 11
profits = []

# Simulacion
for _ in range(iterations):
  demand = getDemand(X)
  cost = offer * 1.5
  
  # Se verifican cuantos 
  offset = offer - demand

  # Si hay mas demanda
  if (0 < offset):
    profit = (demand * 2.5) + (offset * 0.5) - cost
  elif (offset <= 0):
    profit = (offer * 2.5) - cost
  
  profits.append(profit)

profitMean = np.mean(profits)
profitStd = np.std(profits)

print('\n========== Iteraciones:', str(iterations), '==========')
print('Promedio:', round(profitMean, 2))
print('Desviacion Estandar:', round(profitStd, 2), '\n')