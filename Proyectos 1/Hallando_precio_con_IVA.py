def precio (Precio_producto):

    if str(Precio_producto).isdigit() == True:
        Precio_producto = int(Precio_producto)
    
    if str(Precio_producto).isdigit() == False:
        Precio_producto = float(Precio_producto)

    Precio_iva = Precio_producto * 0.19
    
    if Precio_iva % 1 == 0:
        Precio_iva = int(Precio_iva)
    
    if Precio_iva % 1 != 0:
        Precio_iva = float(Precio_iva)

    Precio_producto_final = Precio_producto + Precio_iva

    if Precio_producto_final % 1 == 0:
        Precio_producto_final = int(Precio_producto_final)
        print(f"El precio del producto con IVA es: {Precio_producto_final} pesos")
    
    if Precio_producto_final % 1 != 0:
        Precio_producto_final = float(Precio_producto_final)
        print(f"El precio del producto con IVA es: " + "{:.2f}".format(Precio_producto_final), " pesos")

    if Precio_iva % 1 != 0:
        Precio_iva = float(Precio_iva)
        print(f"El precio del IVA es: " + "{:.2f}".format(Precio_iva), " pesos")

    if Precio_iva % 1 == 0:
        Precio_iva = int(Precio_iva)
        print(f"El precio del IVA es: {Precio_iva} pesos")

precio(input("Digite el precio del producto \n"))
