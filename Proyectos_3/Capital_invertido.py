while True:
    try:
        invertido = float(input("Digite la cantidad a invertir: "))

        if invertido % 1 == 0:
            invertido = int(invertido)
        else:
            invertido = (f"{invertido:g}")
            invertido = float(invertido)
        try:
            interes = float(input("Digite el interes anual: "))

            if interes % 1 == 0:
                interes = int(interes)
            else:
                interes = (f"{interes:g}")
                interes = float(interes)
            try:
                if interes >= invertido:
                    print("El interes no puede ser mayor a lo invertido\n")
                else:
                    años = int(input("Digite el número de años: "))
                    print()
                    for i in range(1, años + 1):
                        invertido = interes + invertido
                        print(f"Su capital en el año {i} es de {invertido} pesos")
                    break
            except:
                print("El año no es válido")
        except:
            print("Valor de interés no válido")
    except:
        print("Valor a invertir no válido")
