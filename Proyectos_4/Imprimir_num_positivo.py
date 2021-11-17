lista_numeros = []

while True:
    try:
        num = float(input("Digite un número: "))
        
        if num % 1 == 0:
            num = int(num)
        else:
            num = (f"{num:g}")
            num = float(num)
        
        if num > 0:
            lista_numeros.append(num)
        else:
            break
    except:
        print("El valor debe ser un número\n")

print("\nLos números que digitó son:\n")

for i in range(len(lista_numeros)):
    if i == len(lista_numeros)-1:
        print(lista_numeros[i], end = "")
    else:
        print(lista_numeros[i], end = ", ")
