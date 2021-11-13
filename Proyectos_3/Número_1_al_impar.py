while True:
    try:
        num = int(input("Digite un número: "))
        print()

        if num <= 0:
            print("El número debe ser positivo")
        else:
            lista_impar = []

            for i in range(1, num+1):
                if i % 2 != 0:
                    lista_impar.append(i)

            for i in lista_impar:
                if i == lista_impar[-1]:
                    print(i, end = "")
                else:
                    print(i, end = ", ")
            break
    except:
        print("\nEl número no es válido")