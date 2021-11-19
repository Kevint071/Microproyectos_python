while True:
    ingresos = float(input("Digite la cantidad de sus ingresos: "))
    casa = 8.8 * 10**7

    if ingresos < 1600000:
        anticipo = casa *  0.15
        pago_mensual = (casa - anticipo) / (15*12)
        if anticipo % 1 == 0:
            anticipo = int(anticipo)
        else:
            anticipo = (f"{anticipo:g}")
            anticipo = float(anticipo)
        break

    elif ingresos >= 1600000:
        anticipo = casa *  0.3
        pago_mensual = (casa - anticipo) / (15*12)

        if anticipo % 1 == 0:
            anticipo = int(anticipo)
        else:
            anticipo = (f"{anticipo:g}")
            anticipo = float(anticipo)
        break

    else:
        print("El número no es válido")
    
print(f"Su anticipo es de: {anticipo}")
print(f"Su pago mensual por 15 años es de: {pago_mensual:g}")