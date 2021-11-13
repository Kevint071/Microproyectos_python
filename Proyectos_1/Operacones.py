from typing import ValuesView

valores = []
i = 1

while i <= 2:
    try:
      x = float(input(f"Digite el número {i}: "))
      valores.append(x) 
      i =i+1
    except:
        print("El dato no es un número válido. Introdúzcalo de nuevo.")
