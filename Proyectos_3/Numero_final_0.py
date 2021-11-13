while True:
    try:
        num = int(input("Digite un número: "))
        print()

        if num <= 0:
            print("El número debe ser positivo\n")
        else:
            for i in range(num, -1, -1):
                if i == 0:
                    print(i, end = "")
                else:
                    print(i, end = ", ")
            break
    except:
        print("El número no es válido\n")