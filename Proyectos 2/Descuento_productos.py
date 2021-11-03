while True:
    try:    
        cantidad = int(input("Digite cuantos productos va a comprar: "))
        print()
        
        while True:
            try:
                precio = float(input("Digite que cuesta cada unidad: $"))
                print()
                if precio % 1 == 0:
                    precio = int(precio)
                else:
                    precio = (f"{precio:g}")
                    precio = float(precio)
                break
            except:
                print("Valor no válido")

        if cantidad <= 20 and cantidad > 10:
            descuento = 0.05

        elif cantidad > 20:
            descuento = 0.1

        elif cantidad < 0:
            print("Valor no válido")
        else:
            descuento = 0

        pago_total = cantidad * precio
        pago_total = pago_total - descuento * pago_total

        if pago_total % 1 == 0:
            pago_total = int(pago_total)
            print(f"El valor a pagar es de: ${pago_total}")
        else:
            print(f"El valor a pagar es de: ${pago_total}")
        break
    except:
        print("El número no es válido")