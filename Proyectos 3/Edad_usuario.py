while True:
    try:
        edad = int(input("Digite su edad: "))

        if edad <= 0:
            print("La edad no es válida\n")
        
        if edad > 0:
            print("\nAños cumplidos: \n")

            for i in range (1, edad + 1):
                if i % 30 == 0:
                    print(i)
                else:
                    if i == edad:
                        print(i)
                    else:
                        print(i, end = ", ")
            break
    except:
        print("La edad no es válida\n")

print(f"\nHa cumplido {edad} años")