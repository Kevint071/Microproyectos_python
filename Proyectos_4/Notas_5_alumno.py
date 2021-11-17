lista_notas = []
lista_notas_unicas = []
lista_notas_alta_baja_media = []

for i in range(1, 6):
    while True:
        nota = float(input(f"Digite la nota {i}: "))
        if nota % 1 == 0:
            nota = int(nota)
        else:
            nota = (f"{nota:g}")
            nota = float(nota)
        
        if nota < 0 or nota > 10:
            print("La nota no es válida\n")
        else:
            lista_notas.append(nota)
            break

print("\nLAS NOTAS SON:\n")
print(lista_notas)

for i in lista_notas:
    if i not in lista_notas_unicas:
        lista_notas_unicas.append(i)

lista_notas_unicas.sort()
redondear = round((len(lista_notas_unicas)-1)/2)

lista_notas_alta_baja_media.append(lista_notas_unicas[0])
lista_notas_alta_baja_media.append(lista_notas_unicas[redondear])
lista_notas_alta_baja_media.append(lista_notas_unicas[-1])

print("\nLAS NOTAS BAJA, MEDIA Y ALTA SON:\n")
print(lista_notas_alta_baja_media)