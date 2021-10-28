while True:
    try:
        num = int(input("Digite un número de 3 cifras: "))

        centena = num // 100
        decena = (num % 100) // 10
        unidad = num % 10

        if num < 100 or num > 999:
            print("El número no es válido")

        else:
            if centena == 2 or centena == 5 or centena == 7:
                num = num + 100

            elif centena == 1 or centena == 4 or centena == 8 or centena == 9:
                num = num - 100
            
            if decena == 2 or decena == 5 or decena == 7:
                num = num + 10
            
            elif decena == 1 or decena == 4 or decena == 8 or decena == 9:
                num = num - 10
            
            if unidad == 2 or unidad == 5 or unidad == 7:
                num = num + 1
            
            elif unidad == 1 or unidad == 4 or unidad == 8 or unidad == 9:
                num = num - 1
            break
    except:
        print("El número no es válido")
    
print(f"El número codificado es {num}")