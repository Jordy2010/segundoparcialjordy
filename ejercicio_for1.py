#Nombre del alumno:Jordy Eduardo Sebastian Lopez
#Ejercicio For:1
#Fecha de elaboración:24-04-2026

#Pedir el nombre del alumno
nombre = input("Ingrese el nombre del alumno: ")

#Inicializar la suma de calificaciones
suma = 0

#Ciclo para leer 7 calificaciones
for i in range(7):
    calif = float(input(f"Ingrese la calificación { i + 1}: "))
    suma += calif

#Calcular el promedio
promedio = suma / 7

#Inprimir el promedio
print(f"El promedio de {nombre} es: {promedio:.2f}")
