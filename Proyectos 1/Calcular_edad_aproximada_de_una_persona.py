import datetime

edad_nacimiento_persona = []

def edad ():
    print("Digite la fecha de nacimiento")
    print("Digite el año: ")
    edad_año = input()
    print("Digite el mes: ")
    edad_mes = input()
    print("Digite el día: ")
    edad_dia = input()
    x = edad_nacimiento_persona.append(edad_año), edad_nacimiento_persona.append(edad_mes), edad_nacimiento_persona.append(edad_dia)
edad()

fecha_actual = datetime.date.today()

años, meses, dias = edad_nacimiento_persona

años = int(años)
meses = int(meses)
dias = int(dias)

fecha_nacimiento = datetime.date(años, meses, dias)

edad_actual_años = fecha_actual.year - fecha_nacimiento.year
edad_actual_meses = fecha_actual.month - fecha_nacimiento.month
edad_actual_dias = fecha_actual.day - fecha_nacimiento.day

if edad_actual_dias < 0:
    edad_actual_meses = edad_actual_meses - 1
    edad_actual_dias = edad_actual_dias + 30
    

if edad_actual_meses < 0:
    edad_actual_años = edad_actual_años - 1
    edad_actual_meses = edad_actual_meses + 12

print(f"Su edad aproximada es de: {edad_actual_años} años, y {edad_actual_meses} meses")