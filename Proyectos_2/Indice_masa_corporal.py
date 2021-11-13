altura = float(input("Digite su estatura(m): "))
peso = float(input("Digite su peso(Kg): "))

if altura % 1 == 0:
    altura = int(altura)
else:
    altura = (f"{altura:g}")
    altura = float(altura)

if peso % 1 == 0:
    peso = int(peso)
else:
    peso = (f"{peso:g}")
    peso = float(peso)

IMC = peso / altura**2

print()
print(f"Su IMC es de {IMC:g}")

if IMC < 18.5:
    print("Por lo tanto su peso es bajo")
elif IMC < 25:
    print("Por lo tanto su peso es normal")
elif IMC < 30:
    print("Por lo tanto tiene sobrepeso")
else:
    print("Por lo tanto tiene obesidad")
print()