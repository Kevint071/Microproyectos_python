while True:
    try:
        num = int(input("Digite un número entero: "))

        if (num % 2 != 0 and num % 3 != 0 and num % 5 != 0 and num % 7 != 0 and num % 11 != 0 and num % 13 != 0) or (2 % num == 0 or 3 % num == 0 or 5 % num == 0 or 7 % num == 0 or 11 % num == 0 or 13 % num == 0):
            print(f"\nEl número {num} es un número primo")
            break
        else:
            print(f"\nEl número {num} no es un número primo")
            break
    except:
        print("El número digitado no es válido\n")
    