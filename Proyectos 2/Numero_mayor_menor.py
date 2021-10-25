num1 = float(input("Digite el número 1: "))
num2 = float(input("Digite el número 2: "))
num3 = float(input("Digite el número 3: "))

if num1 > num2 and num2 > num3:
    print(f"El número 1({num1:g}) es el mayor")
    print(f"El número 3({num3:g}) es el menor ")

elif num1 > num3 and num3 > num2:
    print(f"El número 1({num1:g}) es el mayor")
    print(f"El número 2({num2:g}) es el menor ")

elif num2 > num1 and num1 > num3:
    print(f"El número 2({num2:g}) es el mayor")
    print(f"El número 3({num3:g}) es el menor ")

elif num2 > num3 and num3 > num1:
    print(f"El número 2({num2:g}) es el mayor")
    print(f"El número 1({num1:g}) es el menor ")

elif num3 > num1 and num1 > num2:
    print(f"El número 3({num3:g}) es el mayor")
    print(f"El número 2({num2:g}) es el menor ")

else:
    print(f"El número 3({num3:g}) es el mayor")
    print(f"El número 1({num1:g}) es el menor ")
