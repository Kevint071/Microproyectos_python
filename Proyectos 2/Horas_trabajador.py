while True:
    try:
        hora_normal = float(input("Digite el precio de las horas normales: "))

        if hora_normal % 1 == 0:
            hora_normal = int(hora_normal)

        else:
            hora_normal = (f"{hora_normal:g}")
            hora_normal = float(hora_normal)

        pago_semana = hora_normal * 40
        print()
        break
    except:
        print("Valor no válido")

while True:
    try:
        cantidad_hora_extra = float(input("Digite la cantidad de horas extras trabajadas: "))
        if cantidad_hora_extra % 1 == 0:
            cantidad_hora_extra = int(cantidad_hora_extra)
        else:
            cantidad_hora_extra = (f"{cantidad_hora_extra:g}")
            cantidad_hora_extra = float(cantidad_hora_extra)
        
        if cantidad_hora_extra > 8:
            hora_extra = hora_normal * 3
            hora_extra = cantidad_hora_extra * hora_extra
            
            if hora_extra % 1 == 0:
                hora_extra = int(hora_extra)
            else:
                hora_extra = (f"{hora_extra:g}")
                hora_extra = float(hora_extra)
            break

        elif cantidad_hora_extra <= 8 and cantidad_hora_extra >= 0:
            hora_extra = hora_normal * 2
            hora_extra = cantidad_hora_extra * hora_extra

            if hora_extra % 1 == 0:
                hora_extra = int(hora_extra)
            else:
                hora_extra = (f"{hora_extra:g}")
                hora_extra = float(hora_extra)
            break
        else:
            print("Valor no válido")
    except:
        print("Valor no válido")

print(f"El valor a pagar es de: {pago_semana + hora_extra}")