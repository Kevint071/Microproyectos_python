lista_de_notas = []

def notas ():
    lista_de_notas.clear()
    for i in range (1, 4):
        print("Digite la nota", i)
        nota = input ()
        lista_de_notas.append(nota)
        
    Nota_1, Nota_2, Nota_3 = lista_de_notas

    if Nota_1.isdigit() == False:
        Nota_1 = float(Nota_1)
    
    if Nota_2.isdigit() == False:
        Nota_2 = float(Nota_2)

    if Nota_3.isdigit() == False:
        Nota_3 = float(Nota_3)
    
    if str(Nota_1).isdigit() == True:
        Nota_1 = int(Nota_1)

    if str(Nota_2).isdigit() == True:
        Nota_2 = int(Nota_2)
    
    if str(Nota_3).isdigit() == True:
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
        if Promedio % 1 == 0:
            print(f"El promedio de sus nodas es: {Promedio}")
        if Promedio % 1 != 0:
            print(f"El promedio de sus notas es: ""{:.2f}".format(Promedio))
notas()
