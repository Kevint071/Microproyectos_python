while True:
    nombre = input("Digite el nombre del producto: ")
    lista_nombre = nombre.split(" ")
    nombre_separado = []

    for i in range(0, len(lista_nombre)):
        if lista_nombre[i].isalpha() == True:
            nombre_separado.append(lista_nombre[i])
        if lista_nombre[i].isalpha() == False:
            break
    
    if len(nombre_separado)/len(lista_nombre) == 1:
        break
    else:
        print("Nombre no válido")

while True:
    clave = input("Digite la clave del producto: ")
    if clave == "01":
        dto = 0.1
        break

    elif clave == "02":
        dto = 0.2
        break

    else:
        print()
        print("Clave no válida")

while True:
    precio = float(input("Digite el precio del producto: "))

    if precio <= 0:
        print("Valor no válido")
        print()
    
    else:
        if precio % 1 == 0:
            precio = int(precio)
        
        if precio % 1 != 0:
            precio = (f"{precio:g}")
            precio = float(precio)
        break

precio_final = precio - precio*dto

print()
print("FACTURA")
print()
print(f"Nombre del producto: {nombre}")
print(f"Precio del producto: {precio}")
print(f"Precio del producto con descuento: {precio_final:g}")
print()
