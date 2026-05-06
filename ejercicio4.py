#Nombre del alumno:Jordy Eduardo Sebastian Lopez
#Ejercicio 4:Calcular el número de pulsaciones que una persona debe tener por cada 10 segundos de ejercicio,si la formula es:num pulsaciones=(220 - edad)/10
#Fecha de elaboración:16-04-2026

#Solicitar la edad al usuario
edad = int(input("Introduce tu edad: "))

#Aolicar la fórmula
num_pulsaciones = (220 - edad) / 10

#Mostrar el resultado
print(f"El número de pulsaciones por cada 10 segundos es: {num_pulsaciones}")
