#Nombre del alumno:Jordy Eduardo Sebastian Lopez
#Ejercicio For:2
#Fecha de elaboración:24-04-2026

n = int(input("Ingrese el número de obreros: "))
i = 0
while i < n:
    horas = float(input("Ingrese las horas trabajadas: "))
    if horas <= 40:
        salario = horas * 20
    else:
        salario = 40 * 20 + (horas - 40) * 25
    print("Salario: ", salario)
    i += 1
