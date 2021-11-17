lista_1 = []
lista_2 = []

for j in range(1, 3):
    if j == 1:
        print("LISTA 1\n")
    else:
        print("LISTA 2\n")
    for i in range(1, 6):
        num = int(input(f"Digite el número {i} de la lista {j}: "))
        if i == 5:
            print()
        if j == 1:
            lista_1.append(num)
        else:
            lista_2.append(num)
            
lista_3 = lista_1 + lista_2
print(f"LA SUMA DE LAS DOS LISTAS ES: {lista_3}\n")
print(f"LA SUMA DE LOS VALORES DE LA LISTA 3 ES: {sum(lista_3)}\n")
