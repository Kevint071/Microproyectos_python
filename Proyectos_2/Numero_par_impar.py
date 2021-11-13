while True:
    try:
        num = float(input("Digite un número: "))

        if num % 1 == 0:
            num = int(num)

        else:
            num = (f"{num:g}")
            num = float(num)

        if num > 0:
            if num % 2 == 0:
                print()
                print("El número es par")
            else:
                print()
                print("El número es impar")
            break

        else:
            print()
            print("El número debe ser mayor a 0")
    except:
        print()
        print("El número no es válido")