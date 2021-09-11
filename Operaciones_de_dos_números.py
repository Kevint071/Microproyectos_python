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

operaciones = [Suma, Resta, Mult, Div]
strings = ["suma", "resta", "multiplicación", "división"]

for i in strings:
    x = f"La {i} de los 2 números es: ", operaciones[2]
    print (x)

