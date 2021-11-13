números = [1, 2]
valores = []
for i in números:
    print("Digite el número: ", i)
    x = input()
    valores.append(x)

Num1, Num2 = valores

if float(Num1)%1 != 0:
    Num1 = float(Num1)

if float(Num1)%1 == 0:
    Num1 = int(Num1)

if float(Num2)%1 != 0:
    Num2 = float(Num2)

if float(Num2)%1 == 0:
    Num2 = int(Num2)

Suma = Num1 + Num2
Resta = Num1 - Num2
Mult = Num1 * Num2
Div = Num1 / Num2

if Suma % 1 == 0:
    Suma = int(Suma)
    print(f"La suma de los 2 números es: {Suma}")

if Suma % 1 != 0:
    print(f"La suma de los 2 números es: " + "{:.2f}".format(Suma))
    
if Resta % 1 == 0:
    Resta = int(Resta)
    print(f"La resta de los 2 números es: {Resta}")

if Resta % 1 != 0:
    print(f"La resta de los 2 números es: " + "{:.2f}".format(Resta))
   
if Mult % 1 == 0:
    Mult = int(Mult)
    print(f"La multiplicación de los 2 números es: {Mult}")

if Mult % 1 != 0:
    print(f"La multiplicación de los 2 números es: " + "{:.2f}".format(Mult))

if Div % 1 == 0:
    Div = int(Div)
    print(f"La división de los 2 números es: {Div}")

if Div % 1 != 0:
    print(f"La división de los 2 números es: " + "{:.3f}".format(Div))
