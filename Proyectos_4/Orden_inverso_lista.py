lista_cadena = []
lista_cadena_inversa = []

for i in range(1, 6):
        cadena = input(f"Digite la palabra {i}: ")
        lista_cadena.append(cadena)
print("\nCADENA NORMAL \n")
print(lista_cadena)

for i in range(len(lista_cadena)-1, -1, -1):
    lista_cadena_inversa.append(lista_cadena[i])
print("\nCADENA INVERSA \n")
print(lista_cadena_inversa)
    