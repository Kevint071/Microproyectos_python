lista_de_notas = []

def notas ():
    lista_de_notas.clear()
    for i in range (1, 4):
        print("Digite la nota", i)
        nota = input ()
        lista_de_notas.append(nota)    
    Nota_1, Nota_2, Nota_3 = lista_de_notas
    Nota_1 = int(Nota_1)
    Nota_2 = int(Nota_2)
    Nota_3 = int(Nota_3)
    Suma = Nota_1 + Nota_2 + Nota_3
    Promedio = Suma / 3

    if Nota_1 < 0 or Nota_2 < 0 or Nota_3 < 0:
        print("El valor digitado no es válido")
        print("Digite una nota mayor o igual a 0 y menor o igual a 10")
        notas()
    
    if Nota_1 > 10 or Nota_2 > 10 or Nota_3 > 10:
        print("El valor digitado no es válido")
        print("Digite una nota mayor o igual a 0 y menor o igual a 10")
        notas()
    
    if Nota_1 >= 0 and Nota_1 <= 10 and Nota_2 >= 0 and Nota_2 <= 10 and Nota_3 >= 0 and Nota_3 <= 10:
        print(f"El promedio de sus notas es {Promedio}")
notas()
