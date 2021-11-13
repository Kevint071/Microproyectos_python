print("Por favor, vea nuestro menu de productos: ")

print("\n-------------_/MENU\_-------------\n")
print("1. Leche 1 litro")
print("2. Leche 5 litros")
print("3. Leche 15 litros")
print("4. Leche 18 litros")
print("5. Leche 20 litros\n")

n=int(input(("Selecciona una opción del menu: ")))

if n == 1:
    n=1500
elif n == 2:
    n=3000
elif n == 3:
    n=8000
elif n == 4:
    n=10000
elif n == 5:
    n=15000

di=float(input("Perfecto, ahora por favor ingresa tu codigo de descuento: "))

if di == 0.1:
    di = 0.1
elif di == 0.2:
    di = 0.2

des = di*n
N = n - des

print(f"Su descuento es de: {des:g} Y el valor total a pagar es: {N:5g}")