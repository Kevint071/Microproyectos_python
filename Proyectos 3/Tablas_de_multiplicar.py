for i in range(1, 11):
    if i == 10:
        print(f"TABLA DEL {i}")
    else:
        print(f"TABLA DEL {i}", end = "   ")
print()

lista = []

for i in range(1, 11):
    for j in range(1, 11):

        mult = str(i*j)
        lista = list(mult)
        
        if i == 10:
            print(f"{j} x {i} = {i * j}", end = "   ")
        elif j == 10:
            print(f"{j} x {i} = {i * j}")        
        elif len(lista) == 2:
            print(f"{j} x {i} = {i * j}", end = "    ")
        else:
            print(f"{j} x {i} = {i * j}", end = "     ")