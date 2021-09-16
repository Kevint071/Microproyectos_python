lista_de_números = []

def números ():
    for i in range (1, 6):
        print("Digite el número", i)
        nota = input ()
        lista_de_números.append(nota)
        
    Num_1, Num_2, Num_3, Num_4, Num_5 = lista_de_números

    if Num_1.isdigit() == False:
        Num_1 = float(Num_1)
    
    if Num_2.isdigit() == False:
        Num_2 = float(Num_2)

    if Num_3.isdigit() == False:
        Num_3 = float(Num_3)
    
    if Num_4.isdigit() == False:
        Num_4 = float(Num_4)
    
    if Num_5.isdigit() == False:
        Num_5 = float(Num_5)
    
    if str(Num_1).isdigit() == True:
        Num_1 = int(Num_1)

    if str(Num_2).isdigit() == True:
        Num_2 = int(Num_2)
    
    if str(Num_3).isdigit() == True:
        Num_3 = int(Num_3)
    
    if str(Num_4).isdigit() == True:
        Num_4 = int(Num_4)
    
    if str(Num_5).isdigit() == True:
        Num_5 = int(Num_5)

    Suma = Num_1 + Num_2 + Num_3 + Num_4 + Num_5
    Promedio = Suma / 5

    if Suma % 1 == 0:
        Suma = int(Suma)
        print(f"La suma de los números es: {Suma}")
    if Suma % 1 != 0:
        print(f"La suma de los números es: " + "{:.2f}".format(Suma))

    if Promedio % 1 == 0:
        Promedio = int(Promedio)
        print(f"El promedio de los números es: {Promedio}")
    if Promedio % 1 != 0:
        print(f"El promedio de los números es: " + "{:.2f}".format(Promedio))

números()