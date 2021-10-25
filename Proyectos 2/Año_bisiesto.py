año = int(input("Digite un año: "))

print()

if año % 4 == 0:

    if año % 100 == 0:

        if año % 400 == 0:
            print(f"El año {año} es bisiesto")
        else:
            print(f"El año {año} no es bisiesto")
            
    else:
        print(f"El año {año} es bisiesto")
else:
    print(f"El año {año} no es bisiesto")