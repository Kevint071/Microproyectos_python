while True:

    try:
        print()
        nota = float(input("Digite la nota final del periodo: "))

        if nota % 1 == 0:
            nota = int(nota)

        else:
            nota = (f"{nota:g}")
            nota = float(nota)

        if nota < 30 or nota > 100:
            print()
            print("La nota debe ser mayor o igual a 30 y menor a 100")
        
        if nota >= 30 and nota < 65:
            print()
            print(f"Su promedio es de {nota}, por lo tanto es bajo")
            break

        elif nota >= 65 and nota < 80:
            print()
            print(f"Su promedio es de {nota}, por lo tanto es básico")
            break
        
        elif nota >= 80 and nota < 95:
            print()
            print(f"Su promedio es de {nota}, por lo tanto es alto")
            break

        elif nota >= 95 and nota <= 100:
            print()
            print(f"Su promedio es de {nota}, por lo tanto es superior")
            break
    except:
        print("Valor no válido")