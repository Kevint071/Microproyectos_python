números = [1, 2]
valores = []
for i in números:
    print("Digite el número: ", i)
    x = int(input())
    valores.append(x)

Num1, Num2 = valores

Suma = Num1 + Num2
Resta = Num1 - Num2
Mult = Num1 * Num2
Div = Num1 / Num2

print(f"La suma de los 2 números es: {Suma}")
print(f"La resta de los 2 números es: {Resta}")
print(f"La multiplicación de los 2 números es: {Mult}")
print(f"La división de los 2 números es: {Div}")