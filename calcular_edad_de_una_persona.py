from datetime import date
edad_nacimiento_persona = []

def edad ():
    print("Digite la fecha de nacimiento")
    edad_nacimiento = input()
    x = edad_nacimiento_persona.append(edad_nacimiento)
edad()

print(edad_nacimiento_persona)