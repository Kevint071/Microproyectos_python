import random

lista_valores = []

print("Los valores de su lista con su cuadrado y su cubo son:\n")

for x in range(0, 10):
    aleatorio = random.randint(1, 10)
    cuadrado = aleatorio ** 2
    cubo = aleatorio ** 3
    lista_valores.append([aleatorio, cuadrado, cubo])
print(lista_valores)