números = [1, 2]
valores = []
for i in números:
    print("Digite el número: ", i)
    x = input()
    valores.append(x)

Num1, Num2 = valores

if Num1.isdigit() == False:
    Num1 = float(Num1)

if float(Num1)%1 == 0:
    Num1 = int(Num1)

if Num2.isdigit() == False:
    Num2 = float(Num2)

if float(Num2)%1 == 0:
    Num2 = int(Num2)

Suma = Num1 + Num2
Resta = Num1 - Num2
Mult = Num1 * Num2
Div = Num1 / Num2

if str(Suma).isdigit() == True:
    print(f"La suma de los 2 números es: {Suma}")

if str(Suma).isdigit() == False:
    print(f"La suma de los 2 números es: " + "{:.2f}".format(Suma))
    
if str(Resta).isdigit() == True:
    print(f"La resta de los 2 números es: {Resta}")

if str(Resta).isdigit() == False:
    print(f"La resta de los 2 números es: " + "{:.2f}".format(Resta))
    
if str(Mult).isdigit() == True:
    print(f"La multiplicación de los 2 números es: {Mult}")

if str(Mult).isdigit() == False:
    print(f"La multiplicación de los 2 números es: " + "{:.2f}".format(Mult))

if str(Div).isdigit() == True:
    print(f"La división de los 2 números es: {Div}")

if str(Div).isdigit() == False:
    print(f"La división de los 2 números es: " + "{:.3f}".format(Div))
