N1=int(input("Número 1: "))
N2=int(input("Número 2: "))
N3=int(input("Número 3: "))
N4=int(input("Número 4: "))

if N1>N2:
    if N1>N3:
        if N1>N4:
            print(N1," es el mayor ")
        else:
            if N1==N4:
                print(N1,"y",N4," es los mayores ")
            else:
                print(N4," es el mayor ")
    else:
        if N1==N3:
            if N3>N4:
                print(N1,"y",N3," es los mayores ")
            else:
                print(N4," es el mayor ")
        else:
            if N3>N4:
                print(N3," es el mayor ")
            else:
                print(N4," es el mayor ")
else:
    if N2>N3:
        if N2>N4:
            print(N2," es el mayor ")
        else:
            if N2==N4:
                print(N2,"y",N4," es los mayores ")
            else:
                print(N4," es el mayor ")
    else:
        if N2==N3:
            if N2>N4:
                print(N2,"y",N3," es los mayores ")
            else:
                print(N4," es el mayor ")
        else:
            if N3>N4:
                print(N3," es el mayor ")
            else:
                print(N4," es el mayor ")