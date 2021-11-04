while True:
    palabra = input("Digite una palabra: ")

    palabra_dividida = palabra.split(" ")
    palabra_unida = "".join(palabra_dividida)

    if palabra_unida.isalpha() == True:
        print()
        for i in range(1, 11):
            print(f"{i}. {palabra}")
        print()
        break
    else:
        print("La palabra no es válida\n")