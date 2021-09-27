valores = []
i = 1
while i <= 2:
    try:
      x = float(input(f"Digite el número {i}: "))
      valores.append(x) 
      i += 1
    except ValueError:
      print("El dato no es un número válido. Introdúzcalo de nuevo.")

Num1, Num2 = valores
    
Suma = Num1 + Num2
Resta = Num1 - Num2
Mult = Num1 * Num2
Div = Num1 / Num2

print(f"La suma de los 2 números es: {Suma:g}")
print(f"La resta de los 2 números es: {Resta:g}")
print(f"La multiplicación de los 2 números es: {Mult:g}")
print(f"La división de los 2 números es: {Div:g}")